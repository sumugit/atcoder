N = int(input())
bill_10000 = N//10000
rem = N%10000
bill_5000 = rem//5000
rem %= 5000
bill_1000 = rem//1000
print(bill_10000 + bill_5000 + bill_1000)