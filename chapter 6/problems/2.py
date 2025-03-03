student1 = {
    "sub1" : 56,
    "sub2" : 33,
    "sub3" : 44
}

totalPercent = (student1["sub1"] + student1["sub2"] + student1["sub3"]) // 3

sub1 = student1["sub1"]
sub2 = student1["sub2"]
sub3 = student1["sub3"]

if(totalPercent > 40 and (sub1 >= 33 and sub2 >= 33 and sub3 >= 33)):
    print("you passed")
else:
    print("you failed")