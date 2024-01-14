N = int(input())
def find_good_number(N):
    mapping = {0: '0', 1: '2', 2: '4', 3: '6', 4: '8'}
    good_number_str = ''
    N -= 1
    while N > 0:
        good_number_str = mapping[N % 5] + good_number_str
        N //= 5
    return int(good_number_str) if good_number_str else '0'

print(find_good_number(N))
