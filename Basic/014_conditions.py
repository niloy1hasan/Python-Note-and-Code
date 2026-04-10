# if Elif else
# syntax:
# if condition:
#       statement
# elif condition:
#       statement
# else:
#       statement

a = 25; b=15
if a > b:
    print("a is big")
    print("a: ", a)
elif a < b:
    print("b is big")
    print("b: ", b)
else:
    print("both are equal")


# multiple condition
isRaining = True

if isRaining and a>15:
    print("class is cancel")