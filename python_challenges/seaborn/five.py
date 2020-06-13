#styling
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
tips=sns.load_dataset('tips')
print(tips)
#lx=sns.countplot(x='smoker',data=tips)
#lx=sns.set_context('paper')
#plt.show()
#lx=sns.countplot(x='smoker',data=tips)
#lx=sns.set_context('poster')
#plt.show()
#lx=sns.countplot(x='smoker',data=tips)
#lx=sns.set_context('notebook')
#plt.show()
#lx=sns.countplot(x='smoker',data=tips)
#lx=sns.set_style('whitegrid')
#plt.show()
#lx=sns.countplot(x='smoker',data=tips)
#lx=sns.set_style('ticks')
#plt.show()
lx=sns.countplot(x='smoker',data=tips)
lx=sns.set_style('darkgrid')
plt.show()