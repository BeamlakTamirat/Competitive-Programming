n = int(input())
s = input().strip()
a = s.count('A')
d = s.count('D')
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")