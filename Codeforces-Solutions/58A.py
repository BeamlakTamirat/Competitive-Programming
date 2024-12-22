a=[1,2,3,6,9]
n=len(a)
target=6
x="false"
for i in range(n):
        for j in range(i+1,n):
                if a[i]+a[j]==target:
                        x="true"
                
print(x)