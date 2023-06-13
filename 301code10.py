# Create a new .txt file
file_name = "example.txt"
file = open(file_name, "w")
file.close()

# Append three lines to the file
lines = ["Line 1", "Line 2", "Line 3"]
with open(file_name, "a") as file:
    for line in lines:
        file.write(line + "\n")

# Print the first line
with open(file_name, "r") as file:
    first_line = file.readline()
    print("First line:", first_line)

# Delete the .txt file
import os
os.remove(file_name)
