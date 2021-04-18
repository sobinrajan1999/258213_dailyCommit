def func():
    print("hello world")

func()

#USING ARGUMENT
def func2(word):
    print(word)

func2("hello")         # This way you can use as many argument you want

# RETURN
print("using return")
def func3(x,y):
    return x+y
"""
multiline comment
"""
print(func3(3,5))

# FUNCTIONS AS OBJECTS
print("FUNCTIONS AS OBJECTS")
sum = func3
print(sum(3,5))

def twice(add,x,y):
    return add(add(x,y),add(x,y))

print(twice(func3,4,8))

