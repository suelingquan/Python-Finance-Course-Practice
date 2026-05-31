import matplotlib.pyplot as plt

from matplotlib import rcParams

rcParams['font.family']='SimHei'
rcParams['axes.unicode_minus']=False
growth=[9.8,-3.2,7.1,5.4]
years=[2022,2023,2024,2025]
plt.plot(years,growth,color='blue')

title_font={'family':'Times New Roman','size':16,'weight':'bold'}
label_font={'family':'Times New Roman','size':12}
plt.title("Annual Return sofa Technology Company(%)",fontdict=title_font)
plt.xlabel("Year",fontdict=label_font)
plt.ylabel("AnnualReturn(%)",fontdict=label_font)
plt.xticks(ticks=range(2022,2026,1))

plt.show()
