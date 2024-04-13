S = input()
T = input().lower()

pointer = 0
for s in S:
    if T[pointer] == s:
        pointer += 1
    if pointer == len(T):
        print('Yes')
        exit()
if pointer == len(T) - 1:
    if T[-1] == 'x':
        print('Yes')
        exit()
print('No')