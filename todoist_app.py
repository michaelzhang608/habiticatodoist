from todoist.api import TodoistAPI

api = TodoistAPI("3c2b0a1f2979e9b8f420e2b6bd8b46609faa9c64")
item = api.items.add("TEST")
api.commit()
