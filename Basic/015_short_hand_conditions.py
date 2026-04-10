a = 5; b = 9

# only if
if a>b : print("a is bigger than b")

# if else | ternary operator
print("a is bigger than b") if a>b else print("a is less than or equal to b")

# multiple conditons
print("b") if a>b else print("b") if a<b else print("=")


# assign values with shorthand if else
# variable = value_if_true if condition else value_if_false

big = a if a>b else b

print ("big:", big)

