from decimal import Decimal, getcontext, ROUND_HALF_UP
X, K = map(int, input().split())
s = str(X)
d = Decimal(s)

for i in range(K):
    str_digit = str(1+i) 
    d = Decimal(str(s))
    s = int(d.quantize(Decimal(f'1e{str_digit}'), rounding=ROUND_HALF_UP))
print(s)