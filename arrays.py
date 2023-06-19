import numpy as np
import pandas as pd
t=np.array([[1,2,3,4,5],[4,5,6,56,65],[7,8,9,45,34]])
print(t)
print(t[2,0:4])

data={'roll':[1,2,3,4,5,6],'name':['a','b','c','d','e','f']}
print(data)
df=pd.DataFrame(data)
print(df)
