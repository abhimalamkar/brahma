Here's a generalized prompt template that will guide the generation of code for new tools while adhering to the structure provided:

---

### **Universal Tool Code Generation Prompt**

---

**Description example**:

You are generating a code implementation for a versatile tool based on the following structure and requirements:

### **Tool Structure**:

1. **Base Class**:
    - The tool extends a base class `Tool`, which includes methods for initialization, execution, pre-execution setup, and post-execution response handling.
    - Key methods include:
        - `__init__(self, agent: Agent, name: str, args: dict[str,str], message: str, **kwargs)`: Initializes the tool with its agent, name, arguments, and message.
        - `execute(self, **kwargs)`: The main logic for the tool, which must be implemented in derived classes.
        - `before_execution(self, **kwargs)`: Handles any setup needed before executing the tool.
        - `after_execution(self, response: Response, **kwargs)`: Handles responses after the tool completes its execution.
        - `nice_key(self, key: str)`: A utility method for formatting keys in a readable way.

2. **Tool Implementation**:
    - The derived tool class should override the `execute` method with the specific logic needed for that tool.
    - The tool may involve handling various tasks, such as running code, processing inputs, generating outputs, managing sessions, or interacting with external systems.
    - The implementation should be modular, allowing for easy extension and maintenance.

### **Input Example**:
```json
{
    "tool_name": "data_processing_tool",
    "tool_args": {
        "input_data": "data.csv",
        "operations": [
            {"operation": "filter", "conditions": [{"field": "age", "operator": ">", "value": 30}]},
            {"operation": "map", "fields": ["name", "age", "income"]},
            {"operation": "aggregate", "method": "sum", "field": "income"}
        ],
        "output_format": "JSON"
    }
}
```

### **Output Example** (Python Code):

```python
from abc import abstractmethod
from typing import TypedDict
from agent import Agent
from python.helpers.print_style import PrintStyle
from python.helpers import files, messages

class DataProcessingTool(Tool):

    def execute(self, **kwargs):
        # Initializing and checking preconditions
        self.before_execution(**kwargs)
        
        # Process input data
        input_data = self.args.get("input_data", "")
        operations = self.args.get("operations", [])
        output_format = self.args.get("output_format", "JSON").lower()
        
        # Perform data operations
        processed_data = self.process_data(input_data, operations)
        
        # Generate the final output based on the specified format
        if output_format == "json":
            response = self.generate_json_output(processed_data)
        elif output_format == "csv":
            response = self.generate_csv_output(processed_data)
        else:
            response = "Unsupported output format specified."

        # Handle post-execution steps and return the response
        self.after_execution(Response(message=response, break_loop=False), **kwargs)
        return Response(message=response, break_loop=False)

    def process_data(self, input_data, operations):
        # Logic to handle filtering, mapping, and aggregation
        # Simulating data processing steps
        filtered_data = self.apply_filter(input_data, operations)
        mapped_data = self.apply_mapping(filtered_data, operations)
        aggregated_data = self.apply_aggregation(mapped_data, operations)
        return aggregated_data

    def apply_filter(self, data, operations):
        # Apply filtering logic
        return data  # Placeholder

    def apply_mapping(self, data, operations):
        # Apply mapping logic
        return data  # Placeholder

    def apply_aggregation(self, data, operations):
        # Apply aggregation logic
        return data  # Placeholder

    def generate_json_output(self, data):
        return json.dumps(data, indent=4)

    def generate_csv_output(self, data):
        # Convert data to CSV format
        return "name,age,income\n" + "\n".join([f"{item['name']},{item['age']},{item['income']}" for item in data])

```

### **Guidelines for Generating New Tools**:

1. **Tool Name**: The tool name should reflect its purpose (e.g., `DataProcessingTool`, `WorkflowAutomationTool`).
2. **Execute Logic**: Implement the core functionality within the `execute(self, **kwargs)` method.
3. **Pre-Execution and Post-Execution**: Use `before_execution` and `after_execution` methods to handle any setup or teardown logic.
4. **State Management**: If the tool involves maintaining state or managing sessions, use helper classes or methods to encapsulate that logic.
5. **Output Formatting**: Include options for different output formats (`JSON`, `text`, etc.) based on the tool's requirements.
6. **Modularity**: Organize the tool’s internal logic into helper methods to keep the `execute` method clean and readable.

### **Input query**

{{query}}