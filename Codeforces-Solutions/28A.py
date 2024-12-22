n=int(input())
x=0

if  1<=n<=150:
    for _ in range(n):
        a="++"
        b="--"
        k=input()
        if a in k:
            x=x+1
        elif b in k:
            x=x-1

print(x)  



