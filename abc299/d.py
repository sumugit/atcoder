import sys

N = int(input())
s = 0
e = N-1
prev = -1

def bi_search(s, e, prev):
    ### 終了条件 (ここ忘れて WA) ###
    if e - s <= 1:
        print('! ' + str(s+1))
        exit()
    ##############################
    m = (s+e)//2
    print('? ' + str(m+1))
    sys.stdout.flush()
    res = int(input())
    if m + 1 == e:
        if prev + res == 1:
            print('! ' + str(m))
            exit()
    prev = res
    if res == 1:
        bi_search(s, m, prev)
    elif res == 0:
        bi_search(m, e, prev)

bi_search(s, e, prev)