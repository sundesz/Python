import json
import requests

response = requests.get("https://randomuser.me/api")

data = response.json()

items = json.loads('[{"id": 1, "name": "sandesh"}, {"id": 2, "name": "mandesh"}]')

for item in items:
    print(item)


def greet(greeting, name):
    """[generate greeting]

    Args:
        greeting (string): greeting text
        name (string): name

    Returns:
        [string]: [description]
    """
    return f"{greeting} {name}"


print(greet("hello", "sandesh"))
