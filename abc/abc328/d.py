from collections import Counter, deque, defaultdict

S = list(input())
stack = deque()
abc_cnt = 0
if len(S) < 3:
    print(*S, sep="")
    exit()

stack.append(S[0])
stack.append(S[1])
stack.append(S[2])
for s in S[3:]:
    flag = True
    while flag and len(stack) >= 3:
        fst = stack.pop()
        snd = stack.pop()
        trd = stack.pop()
        if "".join([trd, snd, fst]) != "ABC":
            stack.append(trd)
            stack.append(snd)
            stack.append(fst)
            flag = False
    stack.append(s)

if len(stack) >= 3:
    fst = stack.pop()
    snd = stack.pop()
    trd = stack.pop()
    if "".join([trd, snd, fst]) != "ABC":
        stack.append(trd)
        stack.append(snd)
        stack.append(fst)

print(*stack, sep="")
