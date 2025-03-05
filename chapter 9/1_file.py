# types of file :  
# text file = .txt, .c
# binary file = .jpg, .png, etc

f = open("file.txt","r")
data = f.read()
print(data)
f.close()