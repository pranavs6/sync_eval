import math

def min_jumps(x, y, k):
    # Calculate the required jumps in x and y directions
    required_x = math.ceil(x / k)
    required_y = math.ceil(y / k)
    
    # Simulate the movement
    moves = 0
    current_x, current_y = 0, 0
    while required_x > 0 or required_y > 0:
        if moves % 2 == 0:  # Move along the x-axis
            if required_x > 0:
                current_x += k
                required_x -= 1
        else:  # Move along the y-axis
            if required_y > 0:
                current_y += k
                required_y -= 1
        moves += 1
    
    return moves

# Reading input
t = int(input())
results = []
for _ in range(t):
    x, y, k = map(int, input().split())
    results.append(min_jumps(x, y, k))

# Printing results
for result in results:
    print(result)

