#!/usr/bin/env python3

# Import libraries

import os

# Declaration of variables
directory_path = input("Enter the directory path: ")

### Read user input here into a variable


# Declaration of functions

### Declare a function here

def generate_directory_info(directory_path):
    for (root, dirs, files) in os.walk(directory_path):
        print("Root:", root)
        print("Directories:", dirs)
        print("Files:", files)




# Main


### Pass the variable into the function here

generate_directory_info(directory_path)

# End
