import json


def configOpen(path):
    with open(path, 'r') as file:
        data = file.read()

    return json.loads(data)

