# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits=('Apples','Oranges','Grapes')
#fruits2=tuple(('Apples','Oranges','Grapes'))

# Single value needs trailing comma
fruits2=('Apples',)

# Get value
print(fruits[2])

# Can't change alue
# fruits[0]='Pears'

''' Delete tuple
del fruits2
print(fruits2)
'''

# Get length
print(len(fruits)) 


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set={'Apples','Oranges','Mango'}

# Check if it is in set
print('Apples'in fruits_set)

# Add to set
fruits_set.add('Strawberries')
fruits_set.add('Avocado')
fruits_set.add('Gueverra')
fruits_set.add('Lemons')
fruits_set.add('Blueberries')
print(fruits_set)

# Remove from set
fruits_set.remove('Mango')
print(fruits_set)

# Clear set
fruits_set.clear()

# Delete set
del fruits_set
print(fruits_set)
