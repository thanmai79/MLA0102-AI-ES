import math
def minimax(depth, nodeIndex, isMax, values, maxDepth):
    
    if depth == maxDepth:
        return values[nodeIndex]

    if isMax:
        best = -math.inf
        best = max(best, minimax(depth + 1, nodeIndex * 2, False, values, maxDepth))
        best = max(best, minimax(depth + 1, nodeIndex * 2 + 1, False, values, maxDepth))
        return best

    else:
        best = math.inf

        best = min(best, minimax(depth + 1, nodeIndex * 2, True, values, maxDepth))
        best = min(best, minimax(depth + 1, nodeIndex * 2 + 1, True, values, maxDepth))
        return best
 
values = [2, 3, 5, 9, 0, 1, 7, 5]

maxDepth = 3   

result = minimax(0, 0, True, values, maxDepth)

print("The optimal value is:", result)
