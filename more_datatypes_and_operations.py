#DICTIONARY
ages = {'Sobin': 22, 'Annamma': 61, 'Rajan': 61}
print(ages['Sobin'])
# NOTE: Trying to index a key that isn't part of the dictionary returns a KeyError.

# Trying to use a mutable object as a dictionary key causes a TypeError.
# bad_dict = {[1,2,3]: "one two three"}

squares = {1:2,2:4,3:'error',4:16}
squares[8]=64
squares[9]=81
squares[3]=9
print(squares)

# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
print(64 in squares)

# A useful dictionary method is get.
# It does the same thing as indexing,
# but if the key is not found in the dictionary
# it returns another specified value instead ('None', by default).
print(squares.get(4))
print(squares.get(10,"not in squares"))



#TUPLES
# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.
words = ("spam", "eggs", "sausages")
print(words[2])
# trying to reassign value will give you type error
# Tuples can be created without the parentheses, by just separating the values with commas.
my_tuple = "one","two","three"
print(type(my_tuple))


# LIST SLICING
list1 = [1,2,4,9,16,25,36,49,64,81]
print(list1[2:5])
print(list1[2:10])
print(list1[:7])
print(list1[7:])
print(list1[::2])
print(list1[2:8:2])
print(list1[9:2:-1])

# LIST  COMPREHENSION
cubes = [i**3 for i in range(10)]
print(cubes)

square = [i**2 for i in range(12) if i**2%2==0]
print(square)


# STRING FORMATTING
print("hi there my age is {}".format(22))
print("hi there my age is {}, my mother's name is {} and my father's age is {}".format(22,61,61))
print("hi there my age is {0}, my mother's name is {1} and my father's age is {1}".format(22,61))
print("{x},{y}".format(x=5,y=12))

# STRING FUNCTIONS
print(",".join(['ham','eggs','spams']))
print("Hello There".replace("There",'Sobin'))
print("hello there Sobin".startswith("hello"))
print("hello there sobin".endswith("sobin"))
print("hello there sobin".upper())
print("hello there sobin".lower())


#NUMERIC FUNCTIONS
print(min(1,2,3,4,5,6,7,8,9))
print(max(23,2353,453,4534534,5345,345))
print(abs(-99))
print(sum([1,2,3,4,5,6]))

# ANY AND ALL
if all([i<150 for i in list1]):
    print("all are greater than 150")
if any([i%2==0 for i in list1]):
    print("even number is present")