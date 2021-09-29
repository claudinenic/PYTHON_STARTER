# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor
  def __init__(self, name, email, age, phone):
    self.name=name
    self.email=email
    self.age=age
    self.phone=phone

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age +=1

# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age, phone):
    self.name=name
    self.email=email
    self.age=age
    self.phone=phone
    self.balance=0
  def set_balance(self, balance):
    self.balance=balance

  def greeting(self):
    return f'My name is {self.name}, I am {self.age} years old, My Email is {self.email} with phone number: {self.phone} and my Balance is {self.balance}. '  


# Init  user object
claudine=User('Claudine Nicas','claudinenic@gmail.com',30,'888-888-8888')

# Init customer object
johnson=Customer('Johnson Macoy','johnmacoy@gmail.com', 42, '444-444-4444')

johnson.set_balance(1000)
print(johnson.greeting())

claudine.has_birthday()
print(claudine.greeting())

# print(claudine.age)

