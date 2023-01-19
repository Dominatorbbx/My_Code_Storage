import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
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

sns.pairplot(dataset, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales')
plt.show()