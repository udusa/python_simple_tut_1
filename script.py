


#Hello world
print ("Hello world!")

#variables
myInt = 5
myFloat = 5.0
myString = "string"

print(myInt);print(myFloat);print(myString)
print(myInt+myFloat);print(myFloat+myInt);print(myString+myString)
print(myInt+myInt);
print(myFloat**myInt)

print("my str : %s is in length : %d " % (myString,len(myString)))

#list
mylist = [1,2,"str"]
mylist.append(5)
mylist.append("str2")
print(mylist)
#for item in mylist:
#    print("")
for i in range(len(mylist)):
    print(mylist[i])

#conditions:
x=2
print (x==2);print(x<3);

age = 20
name = "name"
if age==20 and name=="name":
    print("True")
elif age==21:
    print("False")
else:
    print("else")
if age==20 or name=="name":
    print("True")
else:
    print("False")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is in list")

ln1 = [1,2,3];ln2 = [1,2,3]
print(ln1 == ln2);print(ln1 is ln2)

#Strings
str = "Hello world!"
print(str.index("o"))
print(str.count("l"))
print(str[2:8]);print(str[2:8:2]);print(str[::-1]);print(str.upper())
print(str.lower())
print(str.startswith("Hello"))
print(str.endswith("asdfasdfasdf"))
print(str.split(" "))

#loops
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")  # This is the same as count = count + 1

#Functions
def my_function():
    print("Hello From My Function!")
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
def sum_two_numbers(a, b):
    return a + b
my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)

#Dictionary
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264}
phonebook["Jill"] = 947662781
print(phonebook)
#interate
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
del phonebook["John"]
print(phonebook)
phonebook.pop("Jack")
print(phonebook)
if "Jake" not in phonebook:
    print("Jake is not listed in the phonebook.")
if "Jill" in phonebook:
    print("Jill is listed in the phonebook.")


#Read File :
def read_file(fileName):
    file = open(fileName,'r');
    for line in file:
        print(line)
    #print(file.readlines())

read_file("file.txt")