import math

def eratosthenes(N: int) -> list:
    """ N 以下の素数を全て求める (エラトステネスの篩) """
    P = [True] * N
    P[0] = False
    for i in range(2, int(math.sqrt(N)+1)):
        for j in range(i+1, N+1): 
            if j%i == 0:
                P[j-1] = False
    ans = []
    for i in range(1, len(P)):
        if P[i]:
            ans.append(i+1)
    return ans

N = int(input())
print(*eratosthenes(N))