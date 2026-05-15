import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# 1. 加载三张表
# 1.1 公司基本情况表（包含行业分类）
df_company = pd.read_excel(r'D:\Sueling\water_curriculum_homework\python\公司信息文件\TRD_Co.xlsx')

# 1.2 年个股行情表（包含总市值）
df_market = pd.read_excel(r'D:\Sueling\water_curriculum_homework\python\年个股回报率文件\TRD_Year.xlsx')

# 1.3 财务利润表（包含归母净利润）
df_financial = pd.read_csv(r'D:\Sueling\water_curriculum_homework\python\利润表\FS_Comins.csv')

# 2. 数据预处理
# 将所有表中的 Stkcd 转换为字符串类型，避免合并时报错
df_company['Stkcd'] = df_company['Stkcd'].astype(str)
df_market['Stkcd'] = df_market['Stkcd'].astype(str)
df_financial['Stkcd'] = df_financial['Stkcd'].astype(str)
# 2.1 财务数据：筛选合并报表 + 提取年份 + 归母净利润
df_financial = df_financial[df_financial['Typrep'] == 'A'].copy()  # A=合并报表
df_financial['年份'] = pd.to_datetime(df_financial['Accper']).dt.year
df_financial = df_financial[['Stkcd', '年份', 'B002000101']].copy()
df_financial.rename(columns={'B002000101': '净利润_归母'}, inplace=True)

# 删除净利润缺失的记录
df_financial.dropna(subset=['净利润_归母'], inplace=True)

# 2.2 行情数据：提取年份 + 总市值
df_market = df_market[['Stkcd', 'Trdynt', 'Ysmvttl']].copy()
df_market.rename(columns={'Trdynt': '年份'}, inplace=True)

# 注意：Ysmvttl单位是千元，净利润单位是元，后面计算PE时会统一单位
# 删除总市值缺失的记录
df_market.dropna(subset=['Ysmvttl'], inplace=True)

# 2.3 公司行业数据：选择两个行业进行对比
# 示例：选择 0001（金融） 和 0003（房地产）
df_company = df_company[['Stkcd', 'Indcd', 'Indnme']].copy()
df_company.dropna(subset=['Indcd'], inplace=True)

# 筛选两个行业
industry1_code = '0001'   # 金融
industry2_code = '0003'   # 房地产

df_company_selected = df_company[
    (df_company['Indcd'] == industry1_code) |
    (df_company['Indcd'] == industry2_code)
].copy()

print(f"筛选后公司数量: {df_company_selected['Stkcd'].nunique()} 家")
print(f"行业分布:\n{df_company_selected['Indnme'].value_counts()}")

# 3. 数据合并
# 3.1 财务数据 与 行业数据 合并（先拿到每个公司的行业分类）
df_merge = pd.merge(df_financial, df_company_selected, on='Stkcd', how='inner')

# 3.2 再与市值数据合并
df_merge = pd.merge(df_merge, df_market, on=['Stkcd', '年份'], how='inner')

print(f"合并后记录数: {len(df_merge)}")

# 3.3 计算市盈率 PE
# PE = 总市值 / 归母净利润
# Ysmvttl单位是千元，净利润单位是元，需要统一，将净利润转换为千元，或者将市值转换为元，这里统一为千元
df_merge['净利润_归母_千元'] = df_merge['净利润_归母'] / 1000
df_merge['PE'] = df_merge['Ysmvttl'] / df_merge['净利润_归母_千元']

# 3.4 剔除异常值
# 剔除净利润<=0的公司（PE为负或无穷大）
# 剔除PE > 500 或 PE < 0 的极端值
df_merge = df_merge[df_merge['净利润_归母'] > 0]
df_merge = df_merge[(df_merge['PE'] > 0) & (df_merge['PE'] <= 500)]

print(f"剔除异常后记录数: {len(df_merge)}")

# 4. 行业PE聚合（中位数）
# 按年份和行业名称计算PE中位数
industry_pe = df_merge.groupby(['年份', 'Indnme'])['PE'].median().reset_index()

# 重命名行业名称
industry_pe.rename(columns={'Indnme': '行业'}, inplace=True)

# 查看结果
print("\n行业PE年度中位数（前10行）:")
print(industry_pe.head(10))

# 5. 绘制对比趋势图
# 数据透视，方便绘图
pivot_pe = industry_pe.pivot(index='年份', columns='行业', values='PE')

# 删除全为空值的年份
pivot_pe.dropna(how='all', inplace=True)

# 绘图
fig, ax = plt.subplots(figsize=(12, 6))

for industry in pivot_pe.columns:
    ax.plot(pivot_pe.index, pivot_pe[industry], marker='o', linewidth=2, label=industry)

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('市盈率 PE（中位数）', fontsize=12)
ax.set_title(f'{industry1_code} vs {industry2_code} 行业市盈率对比趋势', fontsize=14)
ax.legend()
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

# 设置x轴为整数年份
from matplotlib.ticker import MaxNLocator
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.tight_layout()
plt.show()

#6. 输出统计摘要
print("\n" + "="*60)
print("行业PE统计摘要（全时段）:")
print("="*60)

for industry in pivot_pe.columns:
    print(f"\n【{industry}】")
    print(f"  平均PE: {pivot_pe[industry].mean():.2f}")
    print(f"  中位数PE: {pivot_pe[industry].median():.2f}")
    print(f"  最大PE: {pivot_pe[industry].max():.2f}")
    print(f"  最小PE: {pivot_pe[industry].min():.2f}")

# 保存结果到Excel
output_path = r'D:\Sueling\water_curriculum_homework\python\行业PE对比结果.xlsx'
industry_pe.to_excel(output_path, index=False, engine='openpyxl')
print(f"\n结果已保存到: {output_path}")