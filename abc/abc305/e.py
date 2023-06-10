N = int(input())
a = N//5
b = N/5 - a
if b < 0.5:
    print(5 * a)
else:
    print(5*a + 5)
