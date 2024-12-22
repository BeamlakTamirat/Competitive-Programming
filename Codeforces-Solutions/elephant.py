def min_steps(x):
    # Calculate the number of full 5-unit steps
    steps = x // 5
    
    # If there is any remainder, add one more step
    if x % 5 != 0:
        steps += 1
    
    return steps

# Input reading
x = int(input())

# Output the result
print(min_steps(x))
