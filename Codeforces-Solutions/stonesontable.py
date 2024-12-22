n=int(input())
c=input()



count=0
for i in range(n-1):
    if c[i+1]==c[i]:
        count+=1
    else:
        continue
print(count)


