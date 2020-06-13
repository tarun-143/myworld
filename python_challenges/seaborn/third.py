#types of plots
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
tips=sns.load_dataset('tips')
print(tips)
#kx=sns.countplot(x='day',data=tips)
#plt.show()
lx=sns.pointplot(x='total_bill',y='day',data=tips)
plt.show()
#tx=sns.pointplot(x='tip',y='smoker',data=tips)
#plt.show()
#px=sns.factorplot(x='tip',y='day',data=tips)
#plt.show()
#px=sns.factorplot(x='tip',y='day',data=tips,kind='box')
#plt.show()
#px=sns.factorplot(x='tip',y='day',data=tips,kind='bar')
#plt.show()
#ix=sns.swarmplot(x='smoker',y='tip',data=tips,hue='sex')
#plt.show()
#ix=sns.swarmplot(x='smoker',y='tip',data=tips,hue='sex',palette='cool')
#plt.show()
#ix=sns.boxplot(x='day',y='tip',data=tips)
#plt.show()
#ix=sns.boxplot(x='smoker',y='tip',data=tips,hue='sex')
#plt.show()
#ix=sns.violinplot(x='smoker',y='tip',data=tips,hue='sex')
#plt.show()