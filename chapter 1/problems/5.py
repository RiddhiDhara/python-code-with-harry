# importing os module in python 
import os

# entering the directory path
directory = "/"

# using the os module to list the directory in the path "/"
content = os.listdir(directory)

#  using for loop to print the contents of the content
for i in content:
    print(i)

