import math

S = input()
Q = int(input())
K = list(map(int, input().split()))


def get_character(S, k):
    # ブロック len(S) の反転は 2^k
    N = len(S)
    # T = math.floor(math.log2(k/N+1))
    T = k//N
    relative_index = k%N
    
    original_char = S[relative_index]
    T_bin = bin(T)[2:]
    cnt_1 = T_bin.count('1')
    if cnt_1%2 == 0:
        return original_char
    else:
        if original_char.islower():
            return original_char.upper()
        else:
            return original_char.lower()
    

ans = []
for k in K:
    ans.append(get_character(S, k-1))
print(*ans)