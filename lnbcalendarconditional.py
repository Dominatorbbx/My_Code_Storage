dd = int(input("Enter day:"))
mm = int(input("Enter month:"))
yy = int(input("Enter year:"))

if mm in (11,12,1):
    print("winter season")
elif mm in (2,3,4,5):
    print("summer season")
else:
    print("other season")

if yy%4==0:
    print("leap year")
    print("366 days in a leap year")
else:
    print("not leap year")
    print(int(yy/4)*4 + 4)
