def count():    
    n=int(input())
    total=20

    for _ in range(n):
        x=int(input())
        if 1<=x<=1000 and (x==1 or x==0):
            x=str(x)
            y=int(x[0]+x[1]+x[2])
            if  y>=2:
                total=total+1
            else:
                continue
    print(total)

count()