import re

total = 0
total_chars = 0
encoded_total = 0
with open('8.in') as f:
    lines = [l.strip() for l in f.readlines()]
    # lines = ['""', '"abc"', '"abc\\"aaa"', '"\\x27"']
    for t in lines:
        total += len(t)
        decoded_string = bytes(t, "utf-8").decode("unicode_escape")
        total_chars += len(decoded_string) - 2
        escaped = re.escape(t)
        encoded_string = '"' + escaped.translate(str.maketrans({'"': r'\"'})) + '"'
        encoded_total += len(encoded_string)
print(total - total_chars)
print(encoded_total - total)
