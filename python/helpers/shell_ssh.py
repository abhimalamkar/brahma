import paramiko
import time
import re
import threading
from typing import Optional, Tuple

class SSHInteractiveSession:

    end_comment = "# @@==>> SSHInteractiveSession End-of-Command  <<==@@"
    ps1_label = "SSHInteractiveSession CLI>"
    
    def __init__(self, hostname: str, port: int, username: str, password: str):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.shell = None
        self.full_output = b""  # Still store as bytes
        self.running_command_pid = None
        self.output_thread = None
        self.output_lock = threading.Lock()
        self.command_finished = False

    def connect(self):
        errors = 0
        while True:
            try:
                self.client.connect(self.hostname, self.port, self.username, self.password)
                self.shell = self.client.invoke_shell(width=160, height=48)
                return
            except Exception as e:
                errors += 1
                if errors < 3:
                    print(f"SSH Connection attempt {errors}...")
                    time.sleep(5)
                else:
                    raise e

    def close(self):
        if self.shell:
            self.shell.close()
        if self.client:
            self.client.close()

    def send_command(self, command: str):
        if not self.shell:
            raise Exception("Shell not connected")
        self.full_output = b""
        self.command_finished = False
        
        # Extract the process ID (PID) of the command if possible
        self.shell.send(f"{command} & echo $! \n".encode())
        time.sleep(0.1)
        self.running_command_pid = self.extract_pid()
        
        # Start a background thread to capture output
        self.output_thread = threading.Thread(target=self._capture_output)
        self.output_thread.daemon = True  # Daemon thread will exit when the main program exits
        self.output_thread.start()

    def extract_pid(self):
        time.sleep(0.5)  # Wait for the PID to appear
        output = self.get_latest_output()
        pid = re.search(r'\b\d+\b', output)
        if pid:
            return pid.group()
        return None

    def stop_command(self):
        if self.running_command_pid:
            self.shell.send(f"kill {self.running_command_pid}\n".encode())
            time.sleep(0.1)
            self.running_command_pid = None

    def is_process_running(self):
        if not self.running_command_pid:
            return False
        self.shell.send(f"ps -p {self.running_command_pid}\n".encode())
        time.sleep(0.1)
        output = self.get_latest_output()
        return self.running_command_pid in output

    def _capture_output(self):
        """Continuously capture output in the background and detect when the command finishes."""
        while True:
            if self.shell and self.shell.recv_ready():
                with self.output_lock:
                    partial_output = self.shell.recv(1024)
                    self.full_output += partial_output  # Keep as bytes

                    # Check if the command has finished by detecting the end_comment
                    if SSHInteractiveSession.end_comment.encode() in self.full_output:
                        self.command_finished = True
                        break  # Exit the loop as the command has completed

            if self.command_finished:
                break
            time.sleep(0.1)  # Prevent busy waiting

    def get_latest_output(self):
        """Return the captured output so far."""
        with self.output_lock:
            decoded_output = self.full_output.decode('utf-8', errors='replace')  # Decode bytes to string
            cleaned_output = self.clean_string(decoded_output)
            # Remove the end_comment if it exists
            if SSHInteractiveSession.end_comment in cleaned_output:
                cleaned_output = cleaned_output.split(SSHInteractiveSession.end_comment)[0].strip()
            return cleaned_output

    def clean_string(self, input_string):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        cleaned = ansi_escape.sub('', input_string)
        cleaned = cleaned.replace('\r\n', '\n')
        return cleaned

    def has_command_finished(self):
        return self.command_finished
