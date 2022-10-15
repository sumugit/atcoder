S = list(input())

S[S.index('a')] = 1
S[S.index('t')] = 2
S[S.index('c')] = 3
S[S.index('o')] = 4
S[S.index('d')] = 5
S[S.index('e')] = 6
S[S.index('r')] = 7

def bubble_sort_cnt(data):
    cnt = 0 # 転倒数
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                cnt += 1
    
    return cnt

print(bubble_sort_cnt(S))