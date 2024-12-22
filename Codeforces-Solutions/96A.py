def is_dangerous(situation):
    # Check for seven consecutive '0's or '1's
    if '0000000' in situation or '1111111' in situation:
        return "YES"
    else:
        return "NO"

# Example usage
input_string = input()  # Read input and remove any surrounding whitespace
result = is_dangerous(input_string)
print(result)
