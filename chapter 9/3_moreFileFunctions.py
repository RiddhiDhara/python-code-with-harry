f = open("file1.txt")


lines = f.readlines() # returns list of lines
print(lines, type(lines))
for i in lines:
    print(i)
    
    
#  note 
# f.readline() -> reads only 1 line at a time
# f.readlines() -> reads all lines at once


line1 = f.readline()  # return a string
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)


# ==========using while 

line = f.readline()

while(line != ""):
    print(line)
    

f.close()
    
# ===================modes of opening a file
# syntax = open("file.txt",mode)
# modes: 
# r - read
# w - write
# a - append
# + - open for updating
# rb - open for read in binary mode
# rt - open for read in text mode