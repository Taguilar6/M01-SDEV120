# Defining the function to compare two numbers
def greater_than(x, y):
    if x > y:
        return True
    else:
        return False

# Main section of the program
a = 2
b = 3
result = greater_than(a, b)

# Print the output statement
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

# Test the other scenario by changing values
a = 10
b = 6
result = greater_than(a, b)

# Print the new result
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

