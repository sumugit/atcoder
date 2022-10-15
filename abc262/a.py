Y = int(input())

delta = Y % 4
if delta == 0:
    print(Y + 2)
elif delta == 1:
    print(Y + 1)
elif delta == 2:
    print(Y)
else:
    print(Y+3)