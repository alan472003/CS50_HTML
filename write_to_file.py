# write a program to write a string to a file

# open a file in write mode
f = open("test.txt", "w")

# write a string to the file
f.write("Hello World")

# close the file
f.close()

# open the file in read mode
f = open("test.txt", "r")

# read the contents of the file
print(f.read())

# close the file
f.close()

# Path: read_from_file.py
