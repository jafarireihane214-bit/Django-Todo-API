import requests

# فقط خود رشته توکن (بدون کلمه access و بدون گیومه)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkyOTQwMDczLCJqdGkiOiI0NTE1OGI2OGYwM2E0ODY1OGI1M2M0YjA4NWIzMzQxIiwidXNlcl9pZCI6MX0.7wBzG02DGfTcVnE4KqgGDLtaitXvos6lZ9E_3Hr8wNzA"

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    "title": "تست از پایتون",
    "description": "این تسک از طریق کد ساخته شد"
}

response = requests.post("http://127.0.0.1:8000/api/tasks/", json=data, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.json())