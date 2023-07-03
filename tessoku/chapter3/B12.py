N = int(input())

def check(mid):
    left = mid**3 + mid
    if left >= N:
        return True
    return False

left = 1
right = 100
while right - left > 0.001:
    mid = (left + right) / 2
    if check(mid):
        right = mid
    if not check(mid):
        left = mid + 0.001

print(left)