import requests
import base64

token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

repo = "nelis-dev/api-created-test-repo"

content = base64.b64encode(b"Hello from API file!").decode()

data = {
    "message": "Add hello.txt via API",
    "content": content
}

response = requests.put(
    f"https://api.github.com/repos/{repo}/contents/hello.txt",
    headers=headers,
    json=data
)

print("Status:", response.status_code)
print(response.json())