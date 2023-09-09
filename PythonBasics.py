#exercise 1
#a
print("This line will be printed.")
#b
x = 1
if x == 1:
    
    print("x is 1.")
#exercise 2
#a
myint = 7
print(myint)
#b
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
#c

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
#d
mystring = "Don't worry about apostrophes"
print(mystring)
#f
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
#g
a, b = 3, 4
print(a, b)
#h

one = 1
two = 2
hello = "hello"

print(one, two , hello)
#exercise 3
#a
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) 
print(mylist[1]) 
print(mylist[2]) 


for x in mylist:
    print(x)
#b
mylist = [1,2,3]
print(mylist[2])
#exercise 4 
#a
number = 1 + 2 * 3 / 4.0
print(number)
#b
remainder = 11 % 3
print(remainder)
#c
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
#d
helloworld = "hello" + " " + "world"
print(helloworld)
#e
lotsofhellos = "hello" * 10
print(lotsofhellos)
#f
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
#g
print([1,2,3] * 3)
#exercise 4
#a
name = "John"
print("Hello, %s!" % name)
#b
name = "John"
age = 23
print("%s is %d years old." % (name, age))
#c
mylist = [1,2,3]
print("A list: %s" % mylist)
#exercise 5
#a
astring = "Hello world!"
astring2 = 'Hello world!'
#b
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))
#c
astring = "Hello world!"
print(astring.index("o"))
#d
astring = "Hello world!"
print(astring.count("l"))
#e
astring = "Hello world!"
print(astring[3:7])
#f
astring = "Hello world!"
print(astring[3:7:2])
#g
astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])
#h
astring = "Hello world!"
print(astring[::-1])
#i
astring = "Hello world!"
print(astring.upper())
print(astring.lower())
#j
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
#k
astring = "Hello world!"
afewwords = astring.split(" ")
#exercise 6
#a
x = 2
print(x == 2) 
print(x == 3) 
print(x < 3) 
#b
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
#c
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
#d
statement = False
another_statement = True
if statement is True:
   
    pass
elif another_statement is True: 
   
    pass
else:
    
    pass
#e
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
#f
x = [1,2,3]
y = [1,2,3]
print(x == y) 
print(x is y)
#g
print(not False) 
print((not False) == (False)) 
#exercise 7
#a
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
#b
for x in range(5):
    print(x)


for x in range(3, 6):
    print(x)


for x in range(3, 8, 2):
    print(x)
#c
count = 0
while count < 5:
    print(count)
    count += 1
#d

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


for x in range(10):
    
    if x % 2 == 0:
        continue
    print(x)
#e
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))


for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
#exercise 8
#a
def my_function():
    print("Hello From My Function!")
#b
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
#c
def sum_two_numbers(a, b):
    return a + b
#d

def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

my_function()

my_function_with_args("John Doe", "a great year!")

x = sum_two_numbers(1,2)
#exercise 9 
#a
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
#b
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
#c
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable
#d
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)
#e
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)
#f
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()
#f
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber()) 
#exercise 10
#a
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
#b
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
#c
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
#d
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
#e
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)
#exercise 11
import re


find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))