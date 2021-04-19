#LAMBDAS
# example:
def polynomial(x):
    return x**4 + x*5 + 4
print(polynomial(-4))

print("------in lambda---------")
print((lambda x:x**4 + x*5 +4)(-4))

print("------------------------------")
# Lambda functions can be assigned to variables, and used like normal functions.
var = lambda x: x*x
print(var(4))

print(("-----------MAP------------"))
#MAP
def add(x):
    return x+6
num=[1,2,3,4,5,6]
var = list(map(add,num))
print(var)

#another way
print(list(map((lambda x:x+6),num)))

print("----------FILTER--------------")
#FILTER
print(list(filter(lambda x : x % 2 == 0,num)))


print("-----------GENERATORS----------------")
#GENERATOR
def countdown():
    i=5
    while i>0:
        yield i
        i-=1
# print(list(countdown()))
for i in countdown():
    print(i)


print("--------DECORATOR--------------")
#DECORATOR
def decorator(func):
    def wrap():
        print("------------------------------")
        func()
        print("------------------------------")
    return wrap
def print_text():
    print("Hello World")

decor = decorator(print_text)
decor()
print_text = decorator(print_text)
print_text()


print("-------RECURSION------------")
#RECURSION
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial(5))


print("-----------SETS--------------")
num = {1,2,3,4,5,6}
num.add(7)
num.add(3)
num.remove(1)
print(num)

print("--------------ITERTOOLS------------")
from itertools import count
for i in count(3):
    print(i)
    if i>=11:
        break

from itertools import product, permutations
letters = ['a','b']
print(list(permutations(letters)))
print(list(product(letters,range(2))))