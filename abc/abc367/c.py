N, K = map(int, input().split())
R = list(map(int, input().split()))

# 全探索 + 再帰

def recursive_loops(depth, current_combination, R, N, K):
    if depth == N:
        if sum(current_combination)%K == 0:
            print(*current_combination)
        return
    
    for r in range(1, R[depth] + 1):
        recursive_loops(depth + 1, current_combination + [r], R, N, K)

recursive_loops(0, [], R, N, K)