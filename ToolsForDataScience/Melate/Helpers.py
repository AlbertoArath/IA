import requests
import os

def wget(url: str):
    # Get the file name from the URL
    filename = os.path.basename(url)
    
    # Make a request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to a file in the current directory
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"{filename} has been downloaded successfully.")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
