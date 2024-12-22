n=int(input())
s=str(input())

a=d=0

for i in range(n):
    if s[i]=="A":
        a+=1
    elif s[i]=="D":
        d+=1
    else:
        a==d

#or
#a=s.count("A")
#d=s.count("D")


if a>d:
    print("Anton")
elif a==d:
    print("Friendship")
else:
    print("Danik")


