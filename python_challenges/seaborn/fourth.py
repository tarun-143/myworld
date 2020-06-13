#heatmap
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
iris=sns.load_dataset('iris')
print(iris)
tip=iris.corr()
print(tip)
#px=sns.heatmap(tip)
#plt.show()
#px=sns.heatmap(tip,annot=True)
#plt.show()
#px=sns.heatmap(tip,annot=True,linewidth=8)
#plt.show()
#px=sns.heatmap(tip,annot=True,linewidth=8,linecolor='black')
#plt.show()
#px=sns.heatmap(tip,annot=True,linewidth=8,linecolor='black',cmap='cool')
#plt.show()
#px=sns.heatmap(tip,annot=True,linewidth=8,linecolor='black',cmap='magma')
#plt.show()
px=iris.pivot_table(index='species',columns='sepal_length',values='sepal_width')
hx=sns.heatmap(px,lw=1,annot=True,cmap='cool')
plt.show()