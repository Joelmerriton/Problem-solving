d=int(input())
l=int(input())
r=int(input())
if l<d<r:
    print("yes")
elif d>r:
    print("too late")
else:
    print("too early")
