N, K = map(int, input().split())
S = input()


def split_binary_string_indices(s):
    zeros = []
    ones = []
    current_start = 0
    current_char = s[0]
    start_type = '1' if current_char == '1' else '0'

    for i in range(1, len(s)):
        if s[i] != current_char:
            if current_char == '0':
                # インデックス管理に変更
                zeros.append((current_start, i))
            else:
                ones.append((current_start, i))
            current_char = s[i]
            current_start = i

    if current_char == '0':
        zeros.append((current_start, len(s)))
    else:
        ones.append((current_start, len(s)))

    return zeros, ones, start_type

zeros, ones, start = split_binary_string_indices(S)
result = []
cnt_zeros = 0
cnt_ones = 0

while cnt_zeros < len(zeros) or cnt_ones < len(ones):
    if start == '0' and cnt_zeros < len(zeros):
        start = '1'
        result.append(S[zeros[cnt_zeros][0]:zeros[cnt_zeros][1]])
        cnt_zeros += 1
    elif start == '1' and cnt_ones < len(ones):
        start = '0'
        result.append(S[ones[cnt_ones][0]:ones[cnt_ones][1]])
        cnt_ones += 1
        if cnt_ones == K - 1 and cnt_ones < len(ones) and cnt_zeros < len(zeros):
            result.append(S[ones[cnt_ones][0]:ones[cnt_ones][1]])
            cnt_ones += 1
            result.append(S[zeros[cnt_zeros][0]:zeros[cnt_zeros][1]])
            cnt_zeros += 1

print(''.join(result))
