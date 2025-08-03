# Write a function that takes a single string as input and returns that string in reverse order.
# Define a function called reverse_string that accepts one argument (a string).
# Return the reversed version of the string.
# Try using string slicing as a first approach.

def reverse_string(input_string):
    #Add a feature that ignores whitespace or punctuation
    cleanup = input_string.strip().lower() 
    return cleanup[::-1]

user_input = input("Enter a string to reverse: ")
reversed_output = reverse_string(user_input)
print(f"The reversed of the string is: {reversed_output}")

