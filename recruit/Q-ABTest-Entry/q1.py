from scipy import stats
 
observed = [25, 12, 15, 22, 14, 26, 26]
expected = [20, 20, 20, 20, 20, 20, 20]
 
result = stats.chisquare(observed, expected)
print(result)