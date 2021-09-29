# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON= '{"first_name": "Claudine", "last_name": "Nicas", "age": 28}'

# Parse to dict
user= json.loads(userJSON)

print(user)
print(user['first_name'])

car={'make': 'Ford', 'model': 'Mustang', 'year': 1968}

carJSON=json.dumps(car)

print(carJSON)