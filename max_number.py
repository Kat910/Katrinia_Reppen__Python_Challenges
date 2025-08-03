# Write a function that takes a list of numbers and returns the maximum value in the list — the largest number.
# Define a function called find_max that accepts a list of integers or floats.
# Return the largest number in the list.
# Do not use the built-in max() function — try to solve it manually using:

# Allow the function to work with mixed positive and negative values
# Allow the function to work with mixed positive and negative values
number_list = [1, 2.5, -30, 4.5, 5, 7.8, 7.9] 


def find_max(number_list):
   
# Add error handling for empty lists
  if not number_list:
    print("The list is empty")
    return None
# A variable to track the current maximum
  max_value = number_list[0]
# A for loop to check each number
  for i in range(1, len(number_list)):
    if number_list[i] > max_value:
        max_value = number_list[i]
        max_index = i
    # Return both the max value and its index in the list
  return max_value, max_index

# call the function 
max_value, max_index = find_max(number_list)
print(f"The max number in the list is: {max_value}, and the list index is: {max_index}")



    