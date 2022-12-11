S = input()
if len(S) != 8:
    print('No')
else:
    s1 = S[0]
    try:
        s2 = int(S[1:7])
    except:
        print('No')
        exit()
    s3 = S[7]
    if s1.isupper() and 100000<=s2<=999999 and s3.isupper():
        print('Yes')
    else:
        print('No')