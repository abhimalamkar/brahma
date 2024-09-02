### tool_generator:
This tool generates a new tool by saving a description prompt and the associated Python code into separate files.
The generated description is saved in a folder named `generated_tools/<tool_name>/<tool_name>.md`, and the actual code is saved in `generated_tools/<tool_name>/<tool_name>.py`.
The tool can also call the saved tool and test it by passing in the tool's parameters.

**Important Notes:**
- Each tool should implement an `execute` function, which is the entry point when the tool is called.
- The `execute` function should always return a string.
- When calling a tool, it should only run the `execute` function and nothing else.
- Tools can import necessary libraries such as `datetime` and `pytz`.

**Example usages:**
1. Generate a new tool:
~~~json
{
    "tool_name": "tool_generator",
    "tool_args": {
        "action": "save",
        "tool_name": "example_tool",
        "description": "This is an example tool description...",
        "code": "from datetime import datetime\nimport pytz\ndef execute(args):\n    now = datetime.now(pytz.utc)\n    return f'Executing with args: {args} at {now}'"
    }
}
~~~

2. Call a saved tool:
~~~json
{
    "tool_name": "tool_generator",
    "tool_args": {
        "action": "call",
        "tool_name": "example_tool",
        "args": {"param1": "value1", "param2": "value2"}
    }
}
~~~

3. Test a called tool:
~~~json
{
    "tool_name": "tool_generator",
    "tool_args": {
        "action": "test",
        "tool_name": "example_tool",
        "args": {"param1": "value1", "param2": "value2"}
    }
}
~~~