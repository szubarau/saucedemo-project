import os
import json


BASE_PATH = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(BASE_PATH, "files", "data.json")  # in this example files is a directory name

# Deserialize the data from JSON
with open(path, 'r') as users_data:
    data = json.load(users_data)

USERNAME = data['username']
PASSWORD = data['password']


