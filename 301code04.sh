#!/bin/bash

# Function to display the menu
display_menu() {
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"
    echo
}

# Function to handle user input
handle_input() {
    read -p "Enter your choice (1-4): " choice
    echo

    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    }

    echo
}

# Main loop
while true; do
    display_menu
    handle_input
done
