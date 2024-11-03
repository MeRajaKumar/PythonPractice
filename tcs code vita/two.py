def min_string_factor(X, Y, S, R):
    len_X, len_Y = len(X), len(Y)
    reversed_Y = Y[::-1]
    
    # Initialize dp array with infinity
    dp = [float('inf')] * (len_X + 1)
    dp[0] = 0  # No cost to form an empty string
    
    # Try to form X using substrings from Y and reversed_Y
    for i in range(len_X):
        if dp[i] == float('inf'):
            continue  # Skip if this position is unreachable
        
        # Check for substrings in Y
        for j in range(1, len_Y + 1):
            if i + j > len_X:
                break  # Don't exceed X length
            if X[i:i+j] == Y[:j]:  # If substring of Y matches X[i:i+j]
                dp[i + j] = min(dp[i + j], dp[i] + S)
        
        # Check for substrings in reversed_Y
        for j in range(1, len_Y + 1):
            if i + j > len_X:
                break  # Don't exceed X length
            if X[i:i+j] == reversed_Y[:j]:  # If substring of reversed_Y matches X[i:i+j]
                dp[i + j] = min(dp[i + j], dp[i] + R)
    
    # Result is in dp[len_X] if we could form X, else it's impossible
    return dp[len_X] if dp[len_X] != float('inf') else "Impossible"

# Input reading
X = input().strip()
Y = input().strip()
S, R = map(int, input().split())

# Output the result
print(min_string_factor(X, Y, S, R))
