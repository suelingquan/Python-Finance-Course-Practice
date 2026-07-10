import pandas as pd
import glob
import os

# 数据读取
# 设置工作目录

os.chdir(r'D:\Sueling\water_curriculum_homework\python\大一下期末')
print("工作目录已设置:", os.getcwd())


# 通用读取函数自动尝试多种编码

def read_csv_with_encoding(filepath):
    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030', 'latin1']
    for enc in encodings:
        try:
            df = pd.read_csv(filepath, encoding=enc, dtype={'股票代码': str})
            print(f"  成功使用 {enc} 编码读取")
            return df
        except (UnicodeDecodeError, UnicodeError):
            continue
    # 如果所有编码都失败，尝试跳过错误行
    df = pd.read_csv(filepath, encoding='utf-8', dtype={'股票代码': str},
                     engine='python', on_bad_lines='skip')
    print(f"  使用容错模式读取（跳过部分异常行）")
    return df


# 1. 读取所有个股交易数据

print("\n" + "="*50)
print("1. 读取个股交易数据...")
print("="*50)

stock_files = glob.glob('stock_*.csv')
stock_files = sorted(set(stock_files))

stock_list = []
for f in stock_files:
    print(f"  正在读取: {f}")
    df = read_csv_with_encoding(f)
    stock_list.append(df)
    print(f"  已读取: {f}, {len(df)}行")

stock_df = pd.concat(stock_list, ignore_index=True)
print(f"\n个股数据合并完成: {len(stock_df):,} 行")
print(f"日期范围: {stock_df['日期'].min()} 至 {stock_df['日期'].max()}")
print(f"股票数量: {stock_df['股票代码'].nunique()}")

# 2. 读取所有市值数据

print("\n" + "="*50)
print("2. 正在读取市值数据...")
print("="*50)

marketcap_files = glob.glob('marketcap_*.csv')
marketcap_files = sorted(set(marketcap_files))

marketcap_list = []
for f in marketcap_files:
    print(f"  正在读取: {f}")
    df = read_csv_with_encoding(f)
    marketcap_list.append(df)
    print(f"  已读取: {f}, {len(df)}行")

marketcap_df = pd.concat(marketcap_list, ignore_index=True)
print(f"\n市值数据合并完成: {len(marketcap_df):,} 行")
print(f"日期范围: {marketcap_df['日期'].min()} 至 {marketcap_df['日期'].max()}")


# 3. 读取所有估值数据

print("\n" + "="*50)
print("3. 正在读取估值数据...")
print("="*50)

valuation_files = glob.glob('valuation_*.csv')
valuation_files = sorted(set(valuation_files))

print(f"找到 {len(valuation_files)} 个估值数据文件:")
for f in valuation_files:
    print(f"  - {f}")

valuation_list = []
for f in valuation_files:
    print(f"  正在读取: {f}")
    df = read_csv_with_encoding(f)
    valuation_list.append(df)
    print(f"  已读取: {f}, {len(df)}行")

valuation_df = pd.concat(valuation_list, ignore_index=True)
print(f"\n估值数据合并完成: {len(valuation_df):,} 行")
if len(valuation_df) > 0:
    print(f"日期范围: {valuation_df['日期'].min()} 至 {valuation_df['日期'].max()}")


# 4. 读取辅助数据使用通用编码函数

print("\n" + "="*50)
print("4. 读取辅助数据...")
print("="*50)

# 三因子数据
print("  读取: THRFACDAT_WEEKLY.csv")
ff_df = read_csv_with_encoding('THRFACDAT_WEEKLY.csv')
print(f"三因子数据: {len(ff_df)} 行")

# Shibor数据
print("  正在读取: RESSET_BDSHIBOR.csv")
shibor_df = read_csv_with_encoding('RESSET_BDSHIBOR.csv')
print(f"Shibor数据: {len(shibor_df)} 行")

# 沪深300指数
print("  正在读取: 000300.SH.csv")
hs300_df = read_csv_with_encoding('000300.SH.csv')
print(f"沪深300数据: {len(hs300_df)} 行")


# 5. 查看各数据表的列名

print("\n" + "="*50)
print("5. 各数据表列名预览")
print("="*50)

print("\n【个股数据】列名:", stock_df.columns.tolist())
print("\n【市值数据】列名:", marketcap_df.columns.tolist())
print("\n【估值数据】列名:", valuation_df.columns.tolist())
print("\n【三因子数据】列名:", ff_df.columns.tolist())
print("\n【Shibor数据】列名:", shibor_df.columns.tolist())
print("\n【沪深300数据】列名:", hs300_df.columns.tolist())


# 6. 显示前几行数据

print("\n" + "="*50)
print("6. 各数据表前3行预览")
print("="*50)

print("\n【个股数据】前3行:")
print(stock_df.head(3))

print("\n【市值数据】前3行:")
print(marketcap_df.head(3))

print("\n【估值数据】前3行:")
print(valuation_df.head(3))

print("\n【三因子数据】前3行:")
print(ff_df.head(3))

print("\n【Shibor数据】前3行:")
print(shibor_df.head(3))

print("\n【沪深300数据】前3行:")
print(hs300_df.head(3))

print("\n✅ 所有数据读取成功！")


#数据处理
# 1. 合并个股、市值、估值数据

print("合并数据...")

# 统一列名
stock_df.columns = ['Date', 'Stkcd', 'AdjPrice', 'Volume', 'Amount', 'Turnover']
marketcap_df.columns = ['Date', 'Stkcd', 'TotalMv', 'CircMv']
valuation_df.columns = ['Date', 'Stkcd', 'PE', 'PB']

# 转换日期格式为字符串（便于合并）
stock_df['Date'] = stock_df['Date'].astype(str)
marketcap_df['Date'] = marketcap_df['Date'].astype(str)
valuation_df['Date'] = valuation_df['Date'].astype(str)

# 合并三个表
df = stock_df.merge(marketcap_df, on=['Date', 'Stkcd'], how='inner')
df = df.merge(valuation_df, on=['Date', 'Stkcd'], how='inner')

print(f"合并后数据量: {len(df):,} 行")
print(f"股票数量: {df['Stkcd'].nunique()}")
print(f"日期范围: {df['Date'].min()} 至 {df['Date'].max()}")


# 2. 数据清洗

print("\n正在清洗数据...")

# 剔除成交量为0的股票（停牌）
df = df[df['Volume'] > 0]
print(f"剔除停牌后: {len(df):,} 行")

# 剔除换手率缺失或为0的股票
df = df[df['Turnover'] > 0]
print(f"剔除换手率异常后: {len(df):,} 行")

# 剔除市值缺失的股票
df = df.dropna(subset=['TotalMv', 'CircMv'])
print(f"剔除市值缺失后: {len(df):,} 行")

# 剔除市盈率、市净率为负的异常值
df = df[df['PE'] > 0]
df = df[df['PB'] > 0]
print(f"剔除PE/PB异常后: {len(df):,} 行")


# 3. 转换日期格式并排序

print("\n正在转换日期格式...")
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
df = df.sort_values(['Stkcd', 'Date']).reset_index(drop=True)

print(f"日期范围: {df['Date'].min()} 至 {df['Date'].max()}")


# 4. 计算周收益率

print("\n正在计算周收益率...")
df['Return'] = df.groupby('Stkcd')['AdjPrice'].pct_change()
print(f"收益率计算完成")

# 5. 保存处理后的数据

df.to_csv('processed_data.csv', index=False, encoding='utf-8')
print("\n✅ 处理完成！数据已保存为 'processed_data.csv'")
print(f"最终数据量: {len(df):,} 行")
print(f"股票数量: {df['Stkcd'].nunique()}")
print(f"日期范围: {df['Date'].min()} 至 {df['Date'].max()}")


# 6. 查看数据预览

print("\n数据预览:")
print(df.head(10))
