import requests
import json
from datetime import datetime

# API endpoint
url = "http://localhost:8082/api/send"

# Message data
data = {
    "recipient": "92314311666",
    "message": "EVERYTHING IS OK"
}

# Send the request
response = requests.post(url, json=data)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}") 




# API endpoint for searching contacts
url = "http://localhost:8082/api/search_contacts"

# Contact search query (modify based on your MCP implementation)
data = {
    "query": "Ahad"  # Replace with actual contact name or phone number
}

# Send the request
response = requests.post(url, json=data)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")