import statsmodels.stats.power as smp
print(smp.NormalIndPower().solve_power(effect_size=0.01, alpha=0.05, power=0.8, alternative='two-sided'))
