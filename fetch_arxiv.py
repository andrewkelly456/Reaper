import requests

URL = "https://arxiv.org/list/cs/new"

response = requests.get(
    URL,
    headers={"User-Agent": "Reaper/0.1 (personal project)"},
    timeout=30,
)

print("Status code:", response.status_code)
print("Characters received:", len(response.text))

with open("new.html", "w", encoding="utf-8") as f:
    f.write(response.text)