# Strings in python are surrounded by either single quotation marks, or double quotation marks

# both are same
print('Hello World')
print("Hello World")

# quotation inside qoutation: use as do not match with string's quotation with inner quotation
print("he said, 'I'm learning python.'")

message = "this is an impontant message"
print(message)

# multiline string is surrounded by three quotation """ """   or ''' '''
multiLine = """this is multiline
this is another multiline"""

print(multiLine)

string = "Hello World"
# string's characters are likes array, can access by index
print(string[2])

# loop 

for i in string:
    print(i)
else:
    print("\n")

# string length can get by len() function
print(len(string))

# check membership

print ("world" in string)
print ("world" not in string)
print("Hi" in string)
print("Hi" not in string)