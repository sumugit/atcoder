N = int(input())
ans = hex(N)[2:]
ans = '0' + ans
print(ans[-2:].upper())