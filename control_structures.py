# BOOLEAN AND COMPARISON
x=True
y=False
print(2==3)
print("hello"=='hello')

# Another comparison operator, the not equal operator (!=),
# evaluates to True if the items being compared aren't equal, and False if they are.
print(1!=1)
print("hello"!="world")

# Python also has operators that determine whether one number (float or integer)
# is greater than or smaller than another. These operators are > and < respectively.
print(3>7)
print(3<7)

# Comparison operator <= or >=
print(3<=8)
print(8>=8)

#COMPARISON IF STATEMENT
if(10>5):
    print("10 is greater than 5")
else:
    print("5 is greater than 10")
#Nested if is also possible. elif statement is also present in if statements
num=7
if(num>10):
    print("10")
elif num>5:
    print("greater than 5")
else:
    print("number is")
    print(num)

# BOOLEAN LOGIC
print("different boolean logic")
print(1==1 and 2==2)
print(2==2 and 1==2)
print(1==1 or 2==2)
print(2==2 or 1==2)
print(1==2 or 2==2)
print(1==2 or 2==1)
print(not 1==1)
# This can be use with if statement

#OPERATOR PRECEDENCE - code shows that == has a higher precedence than or
print(False == False or True)
print(False == (False or True))
print((False==False) or True)