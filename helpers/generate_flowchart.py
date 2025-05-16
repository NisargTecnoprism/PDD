from graphviz import Digraph
from collections import defaultdict

def generate_flowchart(data, output_filename="flowchart"):
    dot = Digraph()

    for step in data['steps']:
        node_id = step['id']
        label = step['label']
        shape = step.get('shape', 'rectangle').lower()

        # Default node attributes
        color = "lightblue"
        fontcolor = "black"
        style = "filled"

        # Customize based on shape (type)s
        if "start" in label.lower() or "begin" in label.lower():
            color = "lightgreen"
            shape = "circle"
        elif "end" in label.lower() or "stop" in label.lower():
            color = "lightcoral"
            shape = "circle"
        elif shape == "diamond":
            color = "gold"

        dot.node(node_id, label=label, shape=shape, style=style, fillcolor=color, fontcolor=fontcolor)

    # Add connections (edges) with optional labels
    for connection in data['connections']:
        from_id = connection['from']
        to_id = connection['to']
        label = connection.get('label', '')

        if label:
            dot.edge(from_id, to_id, label=label, fontsize="10", fontcolor="gray20")
        else:
            dot.edge(from_id, to_id)

    dot.render(output_filename, format='png', cleanup=True)
    print(f"Flowchart generated and saved as {output_filename}.png")

if __name__ == "__main__":
    # Example usage
    example_data = {
        "steps": [
            {"id": "Start", "label": "Start", "shape": "oval"},
            {"id": "Login", "label": "Login to system"},
            {"id": "Check", "label": "Check condition", "shape": "diamond"},
            {"id": "End", "label": "End", "shape": "oval"}
        ],
        "connections": [
            {"from": "Start", "to": "Login"},
            {"from": "Login", "to": "Check"},
            {"from": "Check", "to": "End", "label": "Yes"},
            {"from": "Check", "to": "Login", "label": "No"}
        ]
    }
    generate_flowchart(example_data, output_filename="sample_flowchart")
