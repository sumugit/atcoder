S = list(map(int, input().split()))

for i in range(len(S)-1):
    if not ((S[i] <= S[i+1]) and (100 <= S[i] <= 675) and (S[i]%25==0)):
        print("No")
        exit()
if S[len(S)-1]%25 != 0 or (S[len(S)-1] < 100 or S[len(S)-1] > 675):
    print("No")
    exit()
print("Yes")