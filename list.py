words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

# NESTED LIST
a=['string',2,[1,2,"string"],4.24]
print(a[0])
print(a[2])
print(a[2][1])

# 2D list
b=[[1,2,3],[4,5,6],[7,8,9]]
print(b[0][2])
print(b[2][1])

# STRING INDEXING
str="hello world";
print(str[3])

#LIST REASSIGNING
a[2]=3
print(a)

#LIST OPERATIONS
print(words + [1,2,3])
print(words * 3)

#USING IN OPERATOR
print("Hello" in words)
print(5 in b)
print(5 in b[1])

#APPENDING
words.append("hi there")
print(words)

#LIST FUNCTIONS
print(len(words))
# insert
words.insert(2,"Sobin")
print(words)
#index
# words.index('hello')    This will create error
print(words.index("Hello"))

# There are a few more useful functions and methods for lists.
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with minimum value
# list.count(item): Returns a count of how many times an item occurs in a list
# list.remove(item): Removes an object from a list
# list.reverse(): Reverses items in a list.