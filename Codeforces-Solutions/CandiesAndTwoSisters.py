
num=int(input("Enter a number: "));

if(num%2==0):
    a=(num/2)+1;
else:
    a=(num//2)+1;
b=num-a;

count=1;

for i in range(num-a-1):
        b=b-1;
        a+=1;
        count+=1;



print(count);