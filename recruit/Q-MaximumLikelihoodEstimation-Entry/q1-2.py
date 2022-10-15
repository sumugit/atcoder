def f1(x):
    return 2*x

def f2(x):
    if x < 0.5:
        return 4/5
    else:
        return 6/5

x_obs = [0.8, 0.7, 0.9, 0.3, 0.8, 0.15, 0.75, 0.25, 0.3, 0.85]

L_likelihood1 = 1.0
L_likelihood2 = 1.0

for x in x_obs:
    L_likelihood1 *= f1(x)
    L_likelihood2 *= f2(x)

print(L_likelihood1)
print(L_likelihood2)
