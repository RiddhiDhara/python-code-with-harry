with open("this.txt") as t:
    text = t.read()
with open("this_copy.txt","w") as c:
    c.write(text)
    
