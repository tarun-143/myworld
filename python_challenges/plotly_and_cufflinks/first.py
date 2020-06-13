import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.plotly as pl
import cufflinks as cf
import plotly.offline as po

cf.go_offline()
df=pd.DataFrame(np.random.rand(100,5),columns=['a','b','c','d','e'])
di={
	'x':['a','b','c','d','e'],
	'y':['a','b','k','c','k'],
	'z':['a','b','c','d','d']
}
ax=df.iplot(kind='scatter',x='a',y='b')
plt.show()