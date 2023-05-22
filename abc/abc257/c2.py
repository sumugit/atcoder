N=int(input())
S=input()
W=list(map(int,input().split()))
# 文字列は各文字が要素となるように分解される
l=zip(W,S)
# 各タプル先頭の要素でソート
l=sorted(l)
# W, S はタプル
W,S=zip(*l)

sum1 = 0
max1 = 0
# 大人の数
co = S.count('1')
# 子供の数
co1= len(S) - co
sum1 = co
# 左の人 (体重では無い！) から見ていく
for i in range(N):
    # 大人であれば
    if S[i]=="1":
        sum1-=1
    # 子であれば
    else:
        sum1+=1
    # 見ている人が末尾でないとき
    if i<N-1:
        # (ここ重要!) 連続して同じ体重でないとき
        if W[i]!=W[i+1]:
            max1=max(sum1,max1)
# 末尾の人とそれ以外までとの比較
max1=max(co1, co, max1)
print(max1)