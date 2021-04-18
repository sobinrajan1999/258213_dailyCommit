# A variable allows you to store a value by assigning it to a name,
# which can be used to refer to the value later in the program.

# For example, in game development, you would use
# a variable to store the points of the player.
a="Sobin"
# 123var="sboin" This way of naming variable is wrong in python
# Only underscore, alphabet and number is possible

print(a)
print(a*3);

# Reassigning variables
user=4
print(user)

user="This is sting"
print(user + '!')

# INPUT
x=input("Enter string: ")      # it will process input as string. in order to have integer you have to type cast it.
print(x);

x=int(input("enter number: "))
print(x+5)

# INPLACE OPERATOR
x=2
print(x)
x+=3
print(x)
x="spam"
x+='eggs'
print(x)