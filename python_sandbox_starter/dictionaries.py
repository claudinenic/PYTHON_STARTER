# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dictionary
person={
  'first_name':'Claudine',
  'last_name':'Nicas',
  'age':30
}

# Use constructor
# person2=dict(first_name='Amina', last_name='Williams')

# Get value
print(person['first_name'])
# print(person.get('last_name'))

# Add key/value
person['phone']='888-888-8888'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2=person.copy()
person2['city']='Boston'

# Remove item
del(person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people=[
  {'name':'Ray','age':32},
  {'name':'Moris','age':28}
]
print(people[1]['name'])




