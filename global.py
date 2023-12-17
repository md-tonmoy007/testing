# Global variable
global_var = 10

def modify_global_variable():
    # Use the global keyword to indicate that we are modifying the global variable
    print("Inside the function:", global_var)

# Call the function
modify_global_variable()

# Outside the function, the global variable has been modified
print("Outside the function:", global_var)
