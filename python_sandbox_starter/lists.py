# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers=[1,2,3,4,5]
fruits=['Apples','Oranges','Grapes','Pears','Bananas']

# Use a constructor
# numbers2=list((1,2,3,4,5))

# Get a value
print(fruits[2])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')
fruits.append('Papaya')
fruits.append('Maracuja')
print(fruits)

# Remove from list
fruits.remove('Bananas')
print(fruits)

# Insert into position
fruits.insert(4,'Strawberries')
print(fruits)

# Change value
fruits[0]='Blueberries'

# Remove with pop
fruits.pop(5)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)
