import pandas as pd
import scipy.stats as st
df = pd.DataFrame([[14929,1498],   # 紙形式　　　で　記入ありの度数, 記入なしの度数
                   [14911,1628]])  # ウェブ形式　で　記入ありの度数, 記入なしの度数
x2, p, dof, e = st.chi2_contingency(df,correction=False)
print(f'p値 　　　= {p :.3f}')
print(f'カイ2乗値 = {x2:.2f}')
print(f'自由度　  = {dof}')