# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile=open('myfile.txt','w')

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I like Python')
myFile.write(' and Node.js.')
myFile.close()

# Append to file
myFile=open('myfile.txt','a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile=open('myfile.txt','r+')
text=myFile.read(200)
print(text)
