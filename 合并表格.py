import pandas as pd

# 读取两个CSV文件
df1 = pd.read_csv(r'D:\Sueling\water_curriculum_homework\python\return1.csv')
df2 = pd.read_csv(r'D:\Sueling\water_curriculum_homework\python\return2.csv')

# 纵向合并（默认按行拼接）
df_merged = pd.concat([df1, df2], ignore_index=True)

# 保存合并后的文件
df_merged.to_csv('merged_file.csv', index=False)

print(f"合并完成！原始文件1行数：{len(df1)}，文件2行数：{len(df2)}，合并后总行数：{len(df_merged)}")