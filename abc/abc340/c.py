
from functools import lru_cache

N = int(input())

@lru_cache(maxsize=1000)
def recursive(n):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        if n % 2 == 0:
            return n + 2*recursive(n//2)
        else:
            return n + recursive(n//2) + recursive(n//2+1)

print(recursive(N))

# Python 3.9では from functools import cache でメモ化再帰が使える