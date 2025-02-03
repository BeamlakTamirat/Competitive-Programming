n, h = map(int, input().split())
a = list(map(int, input().split()))
width = sum(2 if x > h else 1 for x in a)
print(width)