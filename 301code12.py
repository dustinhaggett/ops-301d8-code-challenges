import requests

# Prompt the user for a URL and HTTP method
url = input("Enter the destination URL: ")
method = input("Select a HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the request details
print(f"\nYou are about to send a {method} request to {url}.")
confirm = input("Do you want to proceed? (yes/no): ")

if confirm.lower() == 'yes':
    # Send the request
    if method.upper() == "GET":
        response = requests.get(url)
    elif method.upper() == "POST":
        response = requests.post(url)
    elif method.upper() == "PUT":
        response = requests.put(url)
    elif method.upper() == "DELETE":
        response = requests.delete(url)
    elif method.upper() == "HEAD":
        response = requests.head(url)
    elif method.upper() == "PATCH":
        response = requests.patch(url)
    elif method.upper() == "OPTIONS":
        response = requests.options(url)
    else:
        print("Invalid HTTP method.")
        exit()

    # Translate the status code
    if response.status_code == 200:
        print("Success!")
    elif response.status_code == 404:
        print("Site not found.")
    else:
        print(f"An error occurred. Status code: {response.status_code}")

    # Print the response headers
    print("\nResponse headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
else:
    print("Request cancelled.")

