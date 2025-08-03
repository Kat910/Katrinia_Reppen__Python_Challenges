# Check for a Palindrome
# Define a function called is_palindrome that accepts a single string.
# Return True if the string is a palindrome, and False otherwise.
# Normalize the string by:
# Converting it to lowercase
# Removing spaces (and optionally punctuation)
# Reverse the normalized string and compare it to the original normalized version.


def is_palindrome(input_string):
    cleanup = input_string.strip().lower() 
    return cleanup[::-1]

user_input = input("Enter a string to check if it's a palindrome: ")
reversed_output = is_palindrome(user_input)
print(f"The reversed of the string is: {reversed_output}")

if user_input.strip().lower() == reversed_output:
    print("Yes, the string is a palindrome.")
else:
    print("No, the string is not a palindrome.")

