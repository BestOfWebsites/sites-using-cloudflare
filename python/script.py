import requests

def http_ping(url):
    try:
        response = requests.get(url, timeout=5)  # Send a GET request with a 5 second timeout
        if response.status_code == 200:
            print(f"Success: {url} is reachable.")
        else:
            print(f"Failed: {url} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not reach {url}. Reason: {e}")

def read_urls_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            urls = file.readlines()
            return [url.strip() for url in urls if url.strip()]  # Remove any extra spaces or newlines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

if __name__ == "__main__":
    file_name = "URL"  # Your file with URLs
    urls = read_urls_from_file(file_name)
    
    if urls:
        for url in urls:
            http_ping(url)
    else:
        print("No URLs to ping.")
