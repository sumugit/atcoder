N = int(input())
H = list(map(int, input().split()))

def compute_T(N, H):
    T = 0 

    for i in range(N):
        H_i = H[i]
        r = T % 3 # 現在のTの余りに応じて場合分け

        q = H_i // 5
        R = H_i % 5

        k_i = 3 * q 

        if R > 0:
            if r == 0:
                if R <= 1:
                    p = 1
                elif R <= 2:
                    p = 2
                else:
                    p = 3
            elif r == 1:
                if R <= 1:
                    p = 1
                elif R <= 4:
                    p = 2
                else:
                    p = 3
            elif r == 2:
                if R <= 3:
                    p = 1
                elif R <= 4:
                    p = 2
                else:
                    p = 3
            k_i += p

        T += k_i

    return T

ans = compute_T(N, H)
print(ans)
