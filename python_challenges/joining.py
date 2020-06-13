import numpy as np
import pandas as pd
x1={'a':[1,2,3],'b':[4,5,6]}
y1={'c':[7,8,9],'d':[6,7,3]}
x=pd.DataFrame(x1,index=['p','q','r'])
y=pd.DataFrame(y1,index=['x','y','z'])
print(x)
print('\n')
print(y)
print('\n')
print(x.join(y,how='right'))
print(x.join(y,how='left'))
print(x.join(y,how='inner'))
print(x.join(y,how='outer'))