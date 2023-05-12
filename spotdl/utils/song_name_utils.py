def format_name(input_str: str) -> str:
    output = input_str

    # ! this is windows specific (disallowed chars)
    output = "".join(char for char in output if char not in "/?\\*|<>#")

    return output.replace('"', "'").replace(":", " - ")
