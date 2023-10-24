N = int(input())
TA = [list(input().split()) for _ in range(N)]
MOD = 10000

board = 0
for T, A in TA:
    if T == '+':
        board += int(A)
        board %= MOD
        print(board)
    elif T == '-':
        board -= int(A)
        board %= MOD
        print(board)
    elif T == '*':
        board *= int(A)
        board %= MOD
        print(board)
