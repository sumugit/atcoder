N = int(input())
S = list(input())

start = False
start_idx = N-1
q_list = []
for i in range(N):
    if not start and S[i] == '"':
        start = True
        start_idx = i
    elif start and S[i] == '"':
        q_list.append((start_idx, i))
        start = False
q_list.append((N, N))

counter = 0
start, end = q_list[counter]
i = 0
while i < N:
    if i < start and S[i] == ',':
        S[i] = '.'
    elif i >= start:
        i = end
        counter += 1
        if counter < len(q_list):
            start, end = q_list[counter]
    i += 1

print(''.join(S))