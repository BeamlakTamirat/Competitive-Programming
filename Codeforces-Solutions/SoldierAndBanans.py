k=int(input("1 banana = $"))
n=int(input("You have :$"))
w=int(input("No'r of Bananas you want: "))

pay=0
borrow=0

for i in range(1,w+1):
    pay=pay + i*k
if pay>n:
    borrow=pay-n
else:
    borrow=0


print(borrow)


