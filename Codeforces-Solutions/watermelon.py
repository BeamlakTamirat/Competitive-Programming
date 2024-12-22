def can_divide_watermelon(w):
    if w % 2 == 0 and w > 2:
        print("YES")
    else:
        print("NO")

# Example usage
w = int(input())
can_divide_watermelon(w)
