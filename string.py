print("hello world");

# Some characters can't be directly included in a string.
# For instance, double quotes can't be directly included
# in a double quote string; this would cause it to end prematurely.
#
# Characters like these must be escaped by placing a backslash before them.
# Double quotes only need to be escaped in double quote strings, and the
# same is true for single quote strings.
print('He\'s a good boy')

# NEWLINE
print('\nHi there\n my name is sobin')

# Newlines will be automatically added for strings that are created using three quotes.
print("""This
 is some
  text""")

# CONCATENATION
print("Sobin"+"Rajan")

# STRING OPERATIONS
print("sobin "*3)
print(4*'2')