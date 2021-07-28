import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename="data/sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(f)
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        high=int(row[5])
        low=int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig,ax=plt.subplots()
ax.plot(dates,highs,alpha=0.5)
ax.plot(dates,lows,alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
ax.set_title("2018年每日最高和最低温度",fontsize=24)
ax.set_xlabel("",fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度 (F)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()