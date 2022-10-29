from functools import lru_cache

N = int(input())
@lru_cache(maxsize=1000)
def f(x):
    if x == 0:
        return 1
    else:
        return f(x//2) + f(x//3)
print(f(N))