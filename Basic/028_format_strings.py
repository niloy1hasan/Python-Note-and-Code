age = 24

# message = "my age is " + age // error, can't concatenate string and number with + operator

# placeholder  f"string {variable call}"

# without f
message = "my age is {age}"
print(message)

# with f
message = f"my age is {age}"
print(message)

price = 120

productPrice = f"this product price is {price} Taka"
print(productPrice)

# decimal point add
productPrice = f"this product price is {price:.2f} Taka"
print(productPrice)

# arithmetic operation inside placeholder
productPrice = f"Total price is {price*3} Taka"
print(productPrice)