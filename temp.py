
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv("homeprices.csv")
print(df)

%matplotlib inline
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')

new_df = df.drop('price',axis='columns')
print(new_df)

model = linear_model.LinearRegression()
model.fit(new_df,df.price)
print(model.fit)

print(model.predict([[3300]]))
print(model.coef_)
print(model.intercept_)

