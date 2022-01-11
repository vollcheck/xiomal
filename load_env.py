from typing import Dict


def load_variables(source: str = ".env") -> Dict[str, str]:
    with open(source, 'r') as f:
        lines = f.readlines()

    variables = {}
    for line in lines:
        k, v = line.split("=")
        variables[k] = v

    return variables


VARIABLES = load_variables()
