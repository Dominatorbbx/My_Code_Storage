import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv(r"C:\Users\ydaks\Downloads\homeprices.csv")
print(df)   
%matplotlib inline
plt.scatter(df.area, df.price, color = 'red')
plt.xlabel('Area in sq.feet') 
plt.ylabel('Price in Rs')
plt.show()  

new_df = df.drop('price', axis=1)
print(new_df)

price = df.price
print(price)

reg = linear_model.LinearRegression()
reg.fit(new_df,price)
print(reg)

print(reg.predict([[4800]]))
      