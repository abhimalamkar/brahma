import os
import importlib.util
from python.helpers.tool import Tool, Response
from python.helpers import files
from agent import Agent

class ToolGenerator(Tool):
    def __init__(self, agent: Agent, name: str, args: dict[str, str], message: str, **kwargs):
        super().__init__(agent, name, args, message, **kwargs)

    def before_execution(self, **kwargs):
        # Any setup logic before execution
        pass

    def execute(self, **kwargs):
        action = self.args.get("action")
        tool_name = self.args.get("tool_name")
        args = self.args.get("args", {})

        self.before_execution(**kwargs)

        if action == "save":
            description = self.args.get("description")
            code = self.args.get("code")
            response = self.save_tool(tool_name, description, code)
        elif action == "call":
            response = self.call_tool(tool_name, args)
        elif action == "test":
            response = self.test_tool(tool_name, args)
        else:
            response = Response(message=f"Invalid action '{action}'. Please specify 'save', 'call', or 'test'.", break_loop=False)

        self.after_execution(response, **kwargs)
        return response

    def after_execution(self, response: Response, **kwargs):
        # Any teardown or response handling after execution
        pass

    def save_tool(self, tool_name: str, description: str, code: str):
        os.makedirs(f"generated_tools/{tool_name}", exist_ok=True)
        # Save description
        with open(f"generated_tools/{tool_name}/{tool_name}.md", "w") as desc_file:
            desc_file.write(description)
        # Save code
        with open(f"generated_tools/{tool_name}/{tool_name}.py", "w") as code_file:
            code_file.write(code)
        return Response(message=f"Tool '{tool_name}' saved successfully.", break_loop=False)

    def call_tool(self, tool_name: str, args: dict):
        tool_path = f"generated_tools/{tool_name}/{tool_name}.py"
        if not os.path.exists(tool_path):
            return Response(message=f"Tool '{tool_name}' not found.", break_loop=True)

        spec = importlib.util.spec_from_file_location(tool_name, tool_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "execute"):
            result = module.execute(args)
            return Response(message=f"Tool output: {result}", break_loop=False)
        else:
            return Response(message=f"Tool '{tool_name}' does not have an 'execute' function.", break_loop=False)

    def test_tool(self, tool_name: str, args: dict):
        try:
            result = self.call_tool(tool_name, args)
            return Response(message=f"Tool '{tool_name}' executed successfully with result: {result.message}", break_loop=True)
        except Exception as e:
            return Response(message=f"An error occurred while testing tool '{tool_name}': {str(e)}", break_loop=False)