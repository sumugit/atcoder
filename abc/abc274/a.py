from decimal import Decimal, getcontext, ROUND_HALF_UP
A, B = map(int, input().split())
s = str(B/A)
d = Decimal(s)
s = str(d.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
print((s+'000')[:5])
