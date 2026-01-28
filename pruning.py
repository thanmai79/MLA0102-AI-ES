import math

def alphabeta(depth, index, isMax, values, maxDepth, alpha, beta):

    if depth == maxDepth:   # terminal node
        return values[index]

    if isMax:
        best = -math.inf

        best = max(best, alphabeta(depth+1, index*2, False, values, maxDepth, alpha, beta))
        alpha = max(alpha, best)

        if beta <= alpha:
            return best

        best = max(best, alphabeta(depth+1, index*2+1, False, values, maxDepth, alpha, beta))
        return best

    else:
        best = math.inf

        best = min(best, alphabeta(depth+1, index*2, True, values, maxDepth, alpha, beta))
        beta = min(beta, best)

        if beta <= alpha:
            return best

        best = min(best, alphabeta(depth+1, index*2+1, True, values, maxDepth, alpha, beta))
        return best


values = [2, 3, 5, 9, 0, 1, 7, 5]
maxDepth = 3

result = alphabeta(0, 0, True, values, maxDepth, -math.inf, math.inf)

print("Optimal value is:", result)
