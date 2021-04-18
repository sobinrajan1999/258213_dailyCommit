try:
    print(7/0)
    print("done calculation")

except ZeroDivisionError:
    print("An error occured")
    print("cannot divide with zero")

print("-------------------------------------------")

try:
    print(3 + " value")
    print(5/0)

except ZeroDivisionError:
    print("cannot divide with zero")

except (ValueError, TypeError):
    print("error occured")
finally:
    print("No matter what this will work")

print("----------------------------")
#RAISING ERROR
print(1)
# raise ValueError

# raise NameError("invlid name")

print("--------------------------------------")
try:
    print(5/0)
except ZeroDivisionError:
    print("error occured")
    # raise
print("--------------------------------------")
#ASSERTIONS
print(1)
assert 1+1==2
print(2)
# assert 2+3==6
print(3)

print("---------------------------------------")
# assert (-10>=0), "colder than expected"