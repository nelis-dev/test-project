import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
print("Token loaded:", token is not None)

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

repo_data = {
    "name": "api-created-test-repo-2",
    "private": False
}

response = requests.post(
    "https://api.github.com/user/repos",
    headers=headers,
    json=repo_data
)

print("Status:", response.status_code)
print(response.json())