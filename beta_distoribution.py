from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
## グラフの表示設定
plt.style.use('ggplot') #グラフスタイル
plt.rcParams['figure.figsize'] = [12, 9] # グラフサイズ
## 計算

D = 6
# for MTD in range(1,7):
# a = max(D-i, 0.5)
b = 0.5
x = np.linspace(0.1, 2, 100) #x軸
# max(D-MTD, 0.5), 1.0
y = beta.pdf(x, 0, 1.0)      #y軸
## グラフ
plt.plot(x, y)
plt.show()