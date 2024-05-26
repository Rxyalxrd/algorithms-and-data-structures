# 114519609 A Python 3.12.1 OK
NUMBER_DIGIT: int = 10


def encrypted_instructions(string: str) -> str:
    """
    Decrypts compressed messages and returns a string of commands.
    c - take a picture;
    в - take a soil sample;
    ш - take a step;
    o - turn on the lights;
    и - initiate terrain scanning.
    Commands can be indicated by Latin or Cyrillic characters.

    Example:
    Command: 2[с]3[в]ш.
    Decoding: «ссвввш».
    Meaning: take two pictures, take three soil samples and make a step.

    Args:
    string (str): The encrypted instruction string.

    Returns:
    str: The decrypted string of commands.
    """

    stack: list[tuple[int, str]] = []
    result: str = ''
    current_num: int = 0

    for char in string:
        if char.isdigit():
            current_num = current_num * NUMBER_DIGIT + int(char)
        elif char == '[':
            stack.append((current_num, result))
            result = ''
            current_num = 0
        elif char.isalpha():
            result += char
        elif char == ']':
            num, prev_string = stack.pop()
            result = prev_string + num * result

    return result


if __name__ == '__main__':
    test_case: str = input()
    print(encrypted_instructions(test_case))
