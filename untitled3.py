import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv(r"D:\IceCreamData.csv")
print(df)
plt.scatter(df.Temperature,df.Revenue, color = 'red')
plt.xlabel("Temperature in C ")
plt.ylabel("Revenue in Rs *100")
plt.show()