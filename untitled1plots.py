import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

slices = [2,4,5]
activities=['Sleeping','Eating','Studying']

plt.pie(slices,labels=activities,colors=['m','b','g'],startangle=90,autopct='%2.1f%%')

plt.title('DaiLy Schedule')
plt.legend()
plt.show()