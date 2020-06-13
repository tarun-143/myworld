import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
tips=sns.load_dataset('tips')
print(tips)
#cx=sns.distplot(tips['size'])
#plt.show()
px=sns.distplot(tips['tip'],kde=False)
plt.show()
#kx=sns.kdeplot(tips['tip'])
#plt.show()