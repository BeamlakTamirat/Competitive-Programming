x=input()

count=0
a=[]

for i in x:
    if i in a:
        continue
    elif i not in a:
        a.append(i)
        count+=1
if len(a)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")



