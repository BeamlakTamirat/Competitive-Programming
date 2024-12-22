n=int(input())

xsum=0
ysum=0
zsum=0
for _ in range(n):
    x,y,z=map(int,input().split())
    xsum=xsum+x
    ysum=ysum+y
    zsum=zsum+z

if xsum==0 and ysum==0 and zsum==0:
            print("yes")
else:
    print("No")


