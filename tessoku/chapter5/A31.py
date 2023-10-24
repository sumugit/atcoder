N = int(input())

ans = 0
ans += N//3
ans += N//5
ans -= N//15
print(ans)