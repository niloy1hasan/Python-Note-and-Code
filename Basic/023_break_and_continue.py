# break keyword used to stop a loop when match with a condition
# continue keyword used when any condition for need to skip, but not break/stop the loop

numList = [4, 2, 9, 1, 5, 3, 12, 8]
search = 12

for i in numList:
    if(search==i):
        print("found")
        break
    print(i)

# print even number
for i in range(1, 21):
    if(i%2==1):
        continue
    print(i, "even number")
        
