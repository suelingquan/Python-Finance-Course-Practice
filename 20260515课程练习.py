
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import platform
# 根据系统自动选择中文字体
system = platform.system()
if system == 'Windows':
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
elif system == 'Darwin': # macOS
    matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC']
else: # Linux
    matplotlib.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False
df = pd.read_excel(r"D:\data.xlsx")
# 精简后的颜色方案（更专业、不刺眼）
colors = [
    '#5E379D',  # 深紫
    '#897CD3',  # 紫
    '#88AFD8',  # 天蓝
    '#90BFCF',  # 浅蓝
    '#AFD1BF',  # 薄荷绿
    '#CFE5BB',  # 草绿
    '#E0EEB8',  # 浅黄绿
    '#9898DC',  # 淡紫
    '#B8BBE7',  # 浅紫
    '#D8DEF7',  # 极浅紫
]

cities = df['city'].unique()
plt.figure(figsize=(16,10))
cities = df['city'].unique()
plt.figure(figsize=(16, 10))

for i, city in enumerate(cities):
    city_data = df[df['city'] == city].sort_values('year')
    color = colors[i % len(colors)]  # 循环使用颜色
    plt.plot(city_data['year'], city_data['ln_Patent1'],
             marker='o', linewidth=2, markersize=4,
             label=city, color=color)

plt.xlabel('年份', fontsize=12)
plt.ylabel('ln_Patent1（专利数对数）', fontsize=12)
plt.title('各城市历年专利数量（对数）变化趋势', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


