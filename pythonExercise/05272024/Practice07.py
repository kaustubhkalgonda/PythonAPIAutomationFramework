# Balance Parenthesis - [{()}]

test_word = "[{(()}]"

count = 0
for char in test_word:
    if char == '[' or char == '{' or char == '(':
        count += 1
    elif char == ']' or char == '}' or char == ')':
        count -= 1

if count != 0:
    print("Unbalanced")
else:
    print("Balanced")
