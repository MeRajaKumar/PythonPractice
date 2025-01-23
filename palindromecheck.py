# method 1
def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]


word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")


# method 2
def is_palindrome(string):
    # Convert to lowercase manually (ASCII-based conversion)
    lower_string = ""
    for char in string:
        if 'A' <= char <= 'Z':  # Check if the character is uppercase
            lower_string += chr(ord(char) + 32)  # Convert to lowercase
        else:
            lower_string += char  # Append as is if already lowercase

    # Remove spaces manually
    processed_string = ""
    for char in lower_string:
        if char != " ":  # Skip spaces
            processed_string += char

    # Check for palindrome using two-pointer approach
    left = 0
    right = len(processed_string) - 1
    while left < right:
        if processed_string[left] != processed_string[right]:
            return False
        left += 1
        right -= 1
    return True

# Test the function
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
