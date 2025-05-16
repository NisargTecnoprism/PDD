import re

def fix_dot_code(dot_code):
    # Inject custom settings into the extracted DOT code
    updated_dot_code = re.sub(
        r'digraph\s+\w*\s*{',
        '''digraph {
    rankdir=TB;
    size="7,5";
    dpi=300;
    ranksep=0.7;
    nodesep=0.3;
    node [shape=box, width=2.5, height=0.8, style=filled, color=lightblue, fontsize=12];''',
        dot_code,
        flags=re.DOTALL
    )
    return updated_dot_code

if __name__ == "__main__":
    # Example usage
    sample_dot = '''
    digraph G {
        Start [shape=oval, label="Start"];
        Process1 [label="Do something"];
        End [shape=oval, label="End"];
        Start -> Process1;
        Process1 -> End;
    }
    '''
    fixed = fix_dot_code(sample_dot)
    print("Modified DOT Code:\n")
    print(fixed)
