# You can use Python to read and write the contents of files.
# Text files are the easiest to manipulate. Before a file can be
# edited, it must be opened, using the open function.

myfile = open("filename.txt")

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

#CLOSING THE FFILE
file = open("filename.txt", "w")
# do stuff to the file
file.close()


#READING FILE
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

# To read only a certain amount of a file, you can provide a number as an argument to the read function.
# This determines the number of bytes that should be read.
# You can make more calls to read on the same file object to read more of the file byte by byte.
# With no argument, read returns the rest of the file.
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# After all contents in a file have been read,
# any attempts to read further from that file will return an empty string,
# because you are trying to read from the end of the file.
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

# To retrieve each line in a file, you can use the readlines
# method to return a list in which each element is a line in the file.

file = open("filename.txt", "r")
print(file.readlines())
file.close()


# You can also use a for loop to iterate through the lines in the file:
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()

# WRITE OPERATION
myfile = open("filename.txt",'w')
myfile.write("hi there this is my first file management")
myfile.close()