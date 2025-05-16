import re

def extract_flowchart_data_from_dot(dot_text):
    steps = []
    connections = []
    step_ids = set()

    # Match nodes: node_id [label="...", shape=...];
    node_pattern = re.compile(r'(\w+)\s*\[\s*label="(.+?)"(?:,\s*shape=(\w+))?.*?];')
    # Match edges: from_node -> to_node [label="..."];
    edge_pattern = re.compile(r'(\w+)\s*->\s*(\w+)(?:\s*\[\s*label="(.*?)"\])?;')

    # Extract nodes
    for match in node_pattern.finditer(dot_text):
        node_id, label, shape = match.groups()
        if node_id not in step_ids:
            step = {
                "id": node_id,
                "label": label.replace("\\n", "\n"),
                "shape": shape if shape else "rectangle"
            }
            steps.append(step)
            step_ids.add(node_id)

    # Extract connections
    for match in edge_pattern.finditer(dot_text):
        from_node, to_node, label = match.groups()
        connection = {
            "from": from_node,
            "to": to_node
        }
        if label:
            connection["label"] = label
        connections.append(connection)

    return {
        "steps": steps,
        "connections": connections
    }

if __name__ == "__main__":
    # Example usage
    sample_dot = '''
    digraph {
        Start [label="Start", shape=oval];
        Step1 [label="Login"];
        Step2 [label="Check Report", shape=diamond];
        End [label="End", shape=oval];
        Start -> Step1;
        Step1 -> Step2;
        Step2 -> End [label="Yes"];
        Step2 -> Step1 [label="No"];
    }
    '''
    result = extract_flowchart_data_from_dot(sample_dot)
    print("Steps:")
    for step in result["steps"]:
        print(step)
    print("\nConnections:")
    for conn in result["connections"]:
        print(conn)
