S = list(input())

ans = [s for s in S if s not in ['a', 'e', 'i', 'o', 'u']]
print(*ans, sep='')