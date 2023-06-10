#!/bin/bash



# Prompt user for input directory path
read -p "Enter the directory path: " directory_path

# Prompt user for input permissions number
read -p "Enter the permissions number (e.g., 777): " permissions

# Navigate to the input directory
cd "$directory_path" || { echo "Directory not found"; exit 1; }

# Change permissions of all files inside the directory
chmod -R "$permissions" .

# Print directory contents and new permissions settings
echo "Directory contents:"
ls -l
