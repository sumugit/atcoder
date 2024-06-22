S_x, S_y = map(int, input().split())
T_x, T_y = map(int, input().split())

y_cost = abs(S_y - T_y)
if (S_x + S_y)%2 == 1 and S_x < T_x:
    S_x -= 1
elif (S_x + S_y)%2 == 0 and S_x > T_x:
    S_x += 1
x_cost = max((abs(S_x - T_x) - y_cost)//2, 0)
ans = y_cost + x_cost
print(ans)