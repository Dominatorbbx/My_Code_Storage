from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

dataset = pd.read_csv('iris.csv')
x = dataset.iloc[:,[1,4]].values
y = dataset.iloc[:,4].values
print(x)
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1,test_size=0.25)
classifier = KNeighborsClassifier(n_neighbors = 4,p=2,metric='euclidean')
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print('confusion matrix is as follows:\n',cm)
print('\n accuracy matrices:')
print(classification_report(y_test, y_pred))
print('correct prediction =',accuracy_score(y_test, y_pred))
print('wrong prediction = ',(1-accuracy_score(y_test, y_pred)))