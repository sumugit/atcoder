H, W = map(int, input().split())

if H==1 or W==1:
    # コーナーケース注意
    print(1)
elif H%2==1 and W%2 == 1:
    print((H*W)//2+1)
else:
    print((H*W)//2)