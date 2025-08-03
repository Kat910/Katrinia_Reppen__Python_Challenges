# Check for a Palindrome
# Define a function called is_palindrome that accepts a single string.
# Return True if the string is a palindrome, and False otherwise.
# Normalize the string by:
# Converting it to lowercase
# Removing spaces (and optionally punctuation)
# Reverse the normalized string and compare it to the original normalized version.

import string

def is_palindrome(input_string):
    # Strip leading/trailing whitespace and convert to lowercase
    clean = input_string.strip().lower()
    
    # Remove all punctuation
    no_punct = clean.translate(str.maketrans('', '', string.punctuation))
    
    # Return both cleaned and reversed strings
    return no_punct, no_punct[::-1]

# Have user input a word to evaluate
user_input = input("Enter a string to check if it's a palindrome: ")

# Set variables to values returned in the function
cleaned, reversed_output = is_palindrome(user_input)

print(f"The cleaned string from entered string is: {cleaned}\nThe reverse of the cleaned string is: {reversed_output}")

if cleaned == reversed_output:
    print("Yes, the string is a palindrome.")
else:
    print("No, the string is not a palindrome.")


