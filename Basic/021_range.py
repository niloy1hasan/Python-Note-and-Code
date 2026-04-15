# range() function return sequence of number, mostly used for looping
# it is immutable, that means can't change values later
# range(start, stop, step)
# range(start, stop)
# ragne(stop)

numbers = range(1, 11, 2)
print(numbers) # immutable, can't see directly
print(list(numbers))

# used to create loop
for i in range(5, 50, 5): print(i)

print(list(range(2, 20, 3)))

# slice
print(numbers[2])
print(list(numbers[:3]))

# membership checking
print(6 in numbers)
print(7 in numbers)
print(len(numbers))
