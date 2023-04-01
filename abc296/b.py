S = [input() for _ in range(8)]
dict_a = {
    8: 'h',
    7: 'g',
    6: 'f',
    5: 'e',
    4: 'd',
    3: 'c',
    2: 'b',
    1: 'a'
}
for i in range(len(S)):
    for j in range(len(S[0])):
        if S[i][j] == '*':
            print(dict_a[j+1] + str(8-i))
            break