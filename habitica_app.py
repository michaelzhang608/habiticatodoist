import requests

auth_headers = {
    "x-api-user": "39515690-ad8c-4c4b-bb78-c23fcaf04b3a",
    "x-api-key": "afe7803a-864b-4c37-9795-b347f3830f98"
}

data = {
    "text": "test",
    "type": "todo"
}
r = requests.post("https://habitica.com/api/v3/tasks/user",json=data, headers=auth_headers)
data = r.json()
print(data)
