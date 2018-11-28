s1=float(input("enter first angle"))
s2=float(input("enter second angle"))
s3=float(input("enter third angle"))
if (s1+s2+s3==180):
    if (s1 == s2 == s3):
        print("given triangle is equilateral triangle")
    else:
        print("given triangle is not an equilateral triangle")
else:
    print("Given shape is not an triangle")
