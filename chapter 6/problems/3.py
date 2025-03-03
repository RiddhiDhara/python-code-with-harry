email1 = "make a lots of money with icici bank loan and investment plans!! click this link "
email2 = "to buy this product now click this link and enjoy your gift and subscribe this channel"
email3 = "here is your custom theme as you have ordered"

spamWordList = ["make a lots of money", "click this", "subscribe this", "buy this" ]

email = email2

if(email.find(spamWordList[0]) != -1 or email.find(spamWordList[1]) != -1 or email.find(spamWordList[2]) != -1 or email.find(spamWordList[3]) != -1):
    print("email is a spam")
else :
    print("email is not spam")