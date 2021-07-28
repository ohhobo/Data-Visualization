import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_values=range(1,1001)
y_values=[x**2 for x in x_values]
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,s=10,c=y_values,cmap=plt.cm.Blues)

ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)

ax.axis([0,1100,0,1100000])

plt.savefig("squares_plot.png",bbox_inches='tight')
plt.show()