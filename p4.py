a=int(input(("enter first no.")))
b=int(input(("enter second no.")))
c=int(input("for addition press1 \n for substraction press 2 \n for multiplication press 3 \n for division press4 \n for remainder press5"))
print()
print()

if c==1:
    print("addition is: ",a+b)
else :
    if c==2:
        print("substraction is: ",a-b)
    else :
        if c==3:
            print("multiplication is: ",a*b)
        else :
            if c==4:
                print("division is: ",a/b)
            else :
                if c==5:
                    print("remainder is: ",a%b)
                else :
                    print("please enter a valid no.")