from datetime import date

name = input("enter name : ")

letter = '''
   Dear <|Name|>,
   You are selected!
   <|Date|>
'''

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",str(date.today()))

# or 
# we can do letter.replace("<|Name|>",name).replace("<|Date|>",str(date.today()))
# this is called chaining

print(letter)