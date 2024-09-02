### tool_generator:
This tool generates a new tool by saving a description prompt and the associated Python code into separate files.
The generated description is saved in a folder named `generated_tools/<tool_name>/<tool_name>.md`, and the actual code is saved in `generated_tools/<tool_name>/<tool_name>.py`.
The tool can also call the saved tool and test it by passing in the tool's parameters.

**Example usages:**
1. Generate a new tool:
~~~json
{
    "thoughts": [
        "I need to generate a new tool named 'example_tool'...",
        "I will save the description and code separately...",
        "The tool should be easily callable and testable..."
    ],
    "tool_name": "tool_generator",
    "tool_args": {
        "tool_name": "example_tool",
        "description": "This is an example tool description...",
        "code": "def example_tool(args):\n    print(f'Executing with args: {args}')"
    }
}
~~~

2. Call a saved tool:
~~~json
{
    "thoughts": [
        "I need to call the previously saved tool 'example_tool' with the appropriate arguments..."
    ],
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
    "thoughts": [
        "I need to test if 'example_tool' works as expected with the given parameters..."
    ],
    "tool_name": "tool_generator",
    "tool_args": {
        "action": "test",
        "tool_name": "example_tool",
        "args": {"param1": "value1", "param2": "value2"}
    }
}
~~~
