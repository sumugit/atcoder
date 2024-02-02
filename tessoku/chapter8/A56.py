N, Q = map(int, input().split())
S = input()
abcd = [list(map(int, input().split())) for _ in range(Q)]

P = 100
MOD = 10**9 + 7
power_of_p = [1] * (N+1)
hash_values = [0] * (N+1)

def get_alphabet_num(c):
    return ord(c) - ord('a') + 1

for i in range(N):
    power_of_p[i+1] = (power_of_p[i] * P) % MOD

for i in range(N):
    hash_values[i+1] = (P * hash_values[i] + get_alphabet_num(S[i])) % MOD # 文字だけでなく位置も考慮

def get_hash(a, b):
    """区間[a, b)のハッシュ値を計算する"""
    val = hash_values[b] - power_of_p[b-a+1]*hash_values[a-1]%MOD
    if val < 0:
        val += MOD
    return val

for a, b, c, d in abcd:
    if get_hash(a, b) == get_hash(c, d):
        print("Yes")
    else:
        print("No")
