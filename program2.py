def is_palindrome(s):
    # Clean the string: remove spaces and convert to lowercase
    clean_s = "".join(s.split()).lower()
    return clean_s == clean_s[::-1]

test_str = "radar"
if is_palindrome(test_str):
    print(f"'{test_str}' is a palindrome")
else:
    print(f"'{test_str}' is not a palindrome")