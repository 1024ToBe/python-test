import numpy as  np
import matplotlib.pyplot as plt  # plot 画板画画
import matplotlib

# Mac 直接用 macosx 后端（原生，不需要tkinter）
matplotlib.use('macosx')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 设置种子
np.random.seed(55)
x = np.random.randn(50)   # 生成随机50个数字
y = x*2 + np.random.randn(50)*0.6  # 在x的技术上y有一点偏移

# 画图
plt.figure(figsize=(8,6))
plt.scatter(x,y,color='red')  # scatter 散点图

plt.title("测试散点图")
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.grid()

plt.show()