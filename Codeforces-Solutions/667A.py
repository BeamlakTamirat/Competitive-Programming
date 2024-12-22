n,h=map(int,input().split())

a=list(map(int,input().split()))

width=0

for i in a:
    if i>h:
        width=width+2
    elif i<=h:
        width=width+1

print(width)

    
