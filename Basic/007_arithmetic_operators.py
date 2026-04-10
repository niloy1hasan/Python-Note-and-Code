# Operators are used to perform operations on variables and values.
# Arithmetic Operators :   + - * / %   ** (Exponentiation, 2 ** 3 = 2^3)  // (floor division)
# // return division value as integer

a = int(input("type first number: "))
b = int(input("type second number: "))

sum = a + b
sub = a - b
multi = a * b
div = a / b
rem = a % b
expo = a ** b
fDiv = a // b

print ("sum : ", sum)
print ("sub :", sub)
print ("multi : ", multi)
print ("div : ", div)
print ("rem : ", rem)
print ("expo : ", expo)
print ("fDiv : ", fDiv)