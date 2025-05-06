
def fibonaccie(a):
    if a <= 1:
        return a
    return fibonaccie(a - 1) + fibonaccie(a - 2)

def countTheNumberOfWays(n):
    ways = fibonaccie(n+1)
    print(ways)
    return ways


n = 100000000
countTheNumberOfWays(n)
