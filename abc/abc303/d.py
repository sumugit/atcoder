X, Y, Z = map(int, input().split())
S = input()

ans = 0
flag = False
char_now = S[0]
sum1 = 0
sum2 = 0
if char_now == 'a':
    sum1 = Z + Y
    sum2 = X
elif char_now == 'A':
    sum1 = Z + X
    sum2 = Y
for i in range(1, len(S)):
    if not flag:
        if (S[i] == char_now) and char_now == 'a':
            sum1 += Y
            sum2 += X
        elif (S[i] == char_now) and char_now == 'A':
            sum1 += X
            sum2 += Y
        else:
            temp = min(sum1, sum2)
            ans += temp
            if temp == sum1:
                flag = True
                if S[i] == 'A':
                    sum1 = Z + Y
                    sum2 = X
                elif S[i] == 'a':
                    sum1 = Z + X
                    sum2 = Y
            else:
                flag = False
                if S[i] == 'a':
                    sum1 = Z + Y
                    sum2 = X
                elif S[i] == 'A':
                    sum1 = Z + X
                    sum2 = Y
    else:
        if (S[i] == char_now) and char_now == 'A':
            sum1 += Y
            sum2 += X
        elif (S[i] == char_now) and char_now == 'a':
            sum1 += X
            sum2 += Y
        else:
            temp = min(sum1, sum2)
            ans += temp
            if temp == sum1:
                flag = False
                if S[i] == 'a':
                    sum1 = Z + Y
                    sum2 = X
                elif S[i] == 'A':
                    sum1 = Z + X
                    sum2 = Y
            else:
                flag = True
                if S[i] == 'A':
                    sum1 = Z + Y
                    sum2 = X
                elif S[i] == 'a':
                    sum1 = Z + X
                    sum2 = Y
    char_now = S[i]


print(ans + min(sum1, sum2))

# 条件分岐のみの実装は基本失敗するので使うな