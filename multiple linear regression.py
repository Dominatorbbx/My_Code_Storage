#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
#Reading the dataset
dataset = pd.read_csv(r"D:\lnb vclasses\advertising.csv")
print(dataset.head())
print(dataset.shape)
print(dataset.isna().sum())
print(dataset.duplicated().any())
fig, axs = plt.subplots(3, figsize =(6,6))
plt1= sns.boxplot(dataset['TV'], ax=axs[0])
plt2= sns.boxplot(dataset['Radio'], ax=axs[1])
plt3= sns.boxplot(dataset['Newspaper'], ax= axs[2])
plt.tight_layout()
plt.show()

sns.distplot(dataset['Sales'],)
plt.show()

#How sales are related with other variables
sns.pairplot(dataset, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales')
plt.show()

#to better visualize it lets make heatplot
sns.heatmap(dataset.corr(), annot = True)
plt.show()

#Simple Linear Model 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
#Setting the value for X and Y
x= dataset[['TV']]
y= dataset[['Sales']]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=100)
slr= LinearRegression()
slr.fit(x_train, y_train)

#Printing the model coefficients
print('Intercept', slr.intercept_)
print('Coefficient', slr.coef_)
print('Regression Equation:Sales = 6.948 + 0.054 * TV')
y_train_predict = slr.predict(x_train)


#Line of the best fit
plt.scatter(x_train['TV'], y_train)
plt.plot(x_train['TV'].to_list(), y_train_predict, 'r')
plt.show()

#Prediction of test and training set result
y_pred_slr= slr.predict(x_test)
x_pred_slr= slr.predict(x_train)
print(y_pred_slr)

#Actual value and the predicted value
slr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_slr})
slr_diff

#Predict for any value
print(slr.predict([[56]]))

# print the R-squared value for the model
from sklearn.metrics import accuracy_score
print('R squared value of the model: {:.2f}'.format(slr.score(x,y)*100))



