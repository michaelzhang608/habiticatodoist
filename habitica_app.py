import requests

auth_headers = {
    "x-api-user": "39515690-ad8c-4c4b-bb78-c23fcaf04b3a",
    "x-api-key": "afe7803a-864b-4c37-9795-b347f3830f98"
}

# 1 hour habit = python

def complete_habitica_todo(taskname):
    data = {
        "text": taskname,
        "type": "todo",
        "value": 1.5,
    }
    r = requests.post("https://habitica.com/api/v3/tasks/user",json=data, headers=auth_headers)
    data = r.json()
    id = data["data"]["id"]
    r = requests.post("https://habitica.com/api/v3/tasks/"+ id +"/score/up", headers=auth_headers)
    print(r)
