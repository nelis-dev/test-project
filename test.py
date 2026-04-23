import requests

token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {token}"
}

response = requests.get("https://api.github.com/user/repos", headers=headers)
data = response.json()

print("Status:", response.status_code)
print("\nYour Repositories:\n")

for repo in data:
    print("Name:", repo["name"])
    print("Private:", repo["private"])
    print("URL:", repo["html_url"])
    print("-" * 40)