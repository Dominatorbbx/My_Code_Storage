import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import statistics
data = {'X': [1, 2, 3, 4, 5], 
        'Y': [3, 4, 2, 6,3]}
df = pd.DataFrame(data)
print(df)

plt.scatter(df.X,df.Y,color='red')
plt.show()


print(statistics.mean([1, 2, 3, 4, 5]))
print(statistics.mean([3, 4, 2, 6,3]))

 
 