import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data= {'Time':[30,20,60],'Calorie':[600,400,1100]}
df=pd.DataFrame(data)
print(df)
df.plot(kind='scatter', x= 'Time',y= 'Calorie')