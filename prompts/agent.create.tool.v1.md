### **Universal Tool Generator Structure**:

```json
{
    "thoughts": [
        "This tool is versatile, allowing for different tasks like querying data, executing operations, and customizing outputs."
    ],
    "tool_name": "universal_tool",
    "tool_args": {
        "query": {
            "type": "information_retrieval",
            "conditions": [
                {"field": "criteria_1", "operator": "==", "value": "value1"},
                {"field": "criteria_2", "operator": "<", "value": 50}
            ],
            "custom_parameters": {
                "page_limit": 10,
                "sort_order": "ascending"
            }
        },
        "execute": [
            {
                "step": 1,
                "action": "data_transformation",
                "input_data": "raw_data.csv",
                "operations": [
                    {"operation": "filter", "conditions": [{"field": "age", "operator": ">", "value": 30}]},
                    {"operation": "map", "fields": ["name", "income"]}
                ]
            },
            {
                "step": 2,
                "action": "generate_report",
                "template": "summary_template",
                "variables": {
                    "title": "Monthly Report",
                    "content_sections": ["Overview", "Detailed Analysis", "Conclusions"]
                }
            }
        ],
        "options": {
            "report_format": "PDF",
            "chart_settings": {
                "type": "bar",
                "color_scheme": "dark",
                "x_axis": "categories",
                "y_axis": "values"
            }
        },
        "tool_output": "Specify 'JSON', 'text', 'HTML', 'PDF'. Default is 'JSON'."
    }
}
```

### **Explanation of Arguments**:

- **`query`**: Use this when you need the tool to retrieve or search information. It can handle conditions, filters, and customized parameters.
  
- **`execute`**: This handles specific actions or operations that involve multiple steps. Each step can define an action, inputs, and parameters.
  
- **`options`**: This section customizes the behavior or output of the tool. It can include settings like report formats, chart styles, or processing options.
  
- **`tool_output`**: Defines the output format, such as JSON, text, HTML, or other formats.

- **`tool_args`**: Provides the content, data, or inputs needed for processing within the tool.

---

### **Example Scenarios for Adaptation**:

1. **Data Transformation and Reporting Tool**:
    - Converts raw data into a report, performing multiple transformations and aggregations.
    - Example: Analyzing sales data, filtering it based on regions and generating a summary report.

2. **Dynamic Content Generator**:
    - Generates structured content based on a user’s preferences like tone, themes, and structure.
    - Example: Writing blog posts with specific keywords, tone, and formatting.

3. **Decision Support System**:
    - Evaluates criteria and provides recommendations based on weighted scoring and decision models.
    - Example: Choosing the best investment options based on cost, ROI, and risk.

4. **Automated Workflow Engine**:
    - Handles a sequence of automated actions with conditional branching.
    - Example: Sending marketing emails, waiting for user responses, and following up accordingly.

5. **Data Aggregation and Visualization Tool**:
    - Aggregates data using various methods and visualizes the results through charts and graphs.
    - Example: Generating interactive dashboards that display key business metrics.

---

### **Final Notes**:
The Universal Tool Generator’s versatility lies in its modular design, which allows it to adapt to a wide range of applications, from data processing and decision-making to content generation and workflow automation. By following this structure, each tool remains consistent, yet flexible enough to meet diverse needs.

### **Input query**

{{query}}