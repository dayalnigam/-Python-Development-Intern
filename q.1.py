#1: Write a Python program to read a file line by line and store it into a list.
with open('myfile.txt') as f:
    content_list = f.readlines()
print(content_list)