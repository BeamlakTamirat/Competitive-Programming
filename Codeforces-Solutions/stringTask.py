a=input()
b=[]

vowel=set("aoyeuiAOYEUI")

for char in a:
    if char not in vowel:
        b.append(".")
        b.append(char.lower())

b=str(''.join(b))

print(b)
    
