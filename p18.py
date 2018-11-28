s1,s2,s3=int((input("enter three angles")).split())
print(s1)
print(s2)
print(s3)
if (s1+s2+s3==180):
    if(s1==s2==s3):
        print("it is an equilateral triangle")
    elif (s1==s2):
        print("it is an isoscales triangle")
    elif (s2==s3):
        print("it is an isoscales triangle")
    elif(s1==s3):
        print("it is an isoscales triangle")
    else:
        print("it is not an isoscales triangle")
else:
    print("given shape is not an triangle")