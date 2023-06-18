import json


data = {"name": "ACME", "shares": 100, "price": 542.23}


with open("helper_files/json.json", "w") as f:
    json.dump(data, f)
