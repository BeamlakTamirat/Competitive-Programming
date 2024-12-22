x=list(input())

l=0
u=0

for i in range(len(x)):
    if x[i].islower():
        l+=1
    elif x[i].isupper():
        u+=1
for i in range(len(x)):
    if u>l:
        x[i]=x[i].upper()
    else:
        x[i]=x[i].lower()
x=''.join(x)

print(x)
