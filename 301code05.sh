#!/bin/bash

# Create backup directory if it doesn't exist
backup_dir="/var/log/backups"
mkdir -p "$backup_dir"

# Get current timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Log files to compress and clear
log_files=(
    "/var/log/syslog"
    "/var/log/wtmp"
)

# Iterate over log files
for file in "${log_files[@]}"; do
    # Print original file size
    file_size=$(du -h "$file" | awk '{print $1}')
    echo "Original file size of $file: $file_size"

    # Compress file to backup directory
    backup_file="$backup_dir/$(basename "$file")-$timestamp.zip"
    zip -q "$backup_file" "$file"

    # Clear log file
    cat /dev/null > "$file"

    # Print compressed file size
    compressed_size=$(du -h "$backup_file" | awk '{print $1}')
    echo "Compressed file size of $backup_file: $compressed_size"

    # Compare sizes
    echo "Size comparison:"
    echo "Original size: $file_size"
    echo "Compressed size: $compressed_size"
    echo
done
