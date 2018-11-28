import os
for x in range(1,4):
    r=int(input("enter pin"))
    if r==1524:
        print("unlocked")
        os._exit(2)
    else:
        print("try again")
print("access stopped")