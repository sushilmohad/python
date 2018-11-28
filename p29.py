import os
for x in range(1,4):
    r = int(input("enter radius"))
    try:
        r=20
    except :
        print("welcome")
        os._exit(2)
    else:
        print("try again")

print("access stoped")
