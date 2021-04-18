# WHILE LOOP
print("while loop")
i=0
while i<=5:
    print(i)
    i+=1

#USING BREAK
print("using break")
i=0
while i<=5:
    if(i==3):
        break;
    print(i)
    i+=1

# For Loop
print("for loop")
for i in range(0,5):
    print(i)

for i in range(10):
    print(i)                   # Print value for 0 to 9

# USING RANGE
print("using range")
for i in range(3,8):
    print(i)
print("print even using range")
for i in range(0,20,2):
    print(i)
for i in range(20,0,-2):
    print(i)

#USING LIST
print("USING LIST")
word=["hello",'world','spam','eggs']
for i in word:
    print(i)