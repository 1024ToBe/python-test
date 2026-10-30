import numpy as  np
import matplotlib.pyplot as plt  # plot 画板画画
import matplotlib

# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
# matplotlib.use('TkAgg')
# Mac 直接用 macosx 后端（原生，不需要tkinter）
matplotlib.use('macosx')
# 注意:中文显示需要额外设置字体
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# Mac自带中文字体：Arial Unicode MS / STHeiti
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

#准备数据
x = np.array([1,2,3,4,5])
y = np.array([10,5,11,3,6])

#画图
#创建画板(空白)
plt.figure(figsize=(8,5)) # 8比5比例画板
#画线
plt.plot(x,y,color='blue')  # 参数1和2 x和y轴数据  plot折线图
# 添加标题
plt.title('测试折线图')
# 给x轴取名字
plt.xlabel('这是X轴')
# 给x轴取名字
plt.ylabel('这是Y轴')
#显示网格
plt.grid()
#显示
plt.show()