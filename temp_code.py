import requests

response = requests.get('https://api.github.com')
print(f"GitHub API Response: {response.status_code}")