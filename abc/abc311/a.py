N = int(input())
S = input()

flag_a, flag_b, flag_c = False, False, False
for idx, s in enumerate(S):
    if s == 'A':
        flag_a = True
    elif s == 'B':
        flag_b = True
    elif s == 'C':
        flag_c = True
    if flag_a and flag_b and flag_c:
        print(idx+1)
        exit()