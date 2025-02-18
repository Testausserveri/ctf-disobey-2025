from itertools import zip_longest

whitespace = open("unusual_indentation.ws").readlines()
result = open("result.rs").readlines()

assert len(whitespace) == len(result)
for i, (ws_line, result_line) in enumerate(zip(whitespace, result)):
    if not all(ws_char == result_char for ws_char, result_char in zip_longest(ws_line, result_line, fillvalue=None) if result_line.isspace()):
        print(f"Problem on line {i+1}")
