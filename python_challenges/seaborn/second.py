import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
tips=sns.load_dataset('tips')
print(tips)
#hx=sns.residplot(x='total_bill',y='tip',data=tips)
#plt.show()
jx=sns.jointplot(x='total_bill',y='tip',data=tips)
plt.show()
#kx=sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')
#plt.show()
#kx=sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
#plt.show()
#kx=sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex',color='#4CB391')
#plt.show()
#kx=sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg',color='#4CB391')
#plt.show()
#lx=sns.pairplot(tips)
#plt.show()
#lx=sns.pairplot(tips,hue='smoker')
#plt.show()
#lx=sns.pairplot(tips,hue='time')
#plt.show()
#lx=sns.pairplot(tips,hue='day')
#plt.show()