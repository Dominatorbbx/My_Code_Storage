import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
plt.bar([0,1,2,3],[20,30,40,50], label ='Jujutsu Kaisen', color = 'r',width=.4)
plt.bar([0.4,1.4,2.4,3.4],[11,12,14,19], label ='My Hero Academia', color = 'k',width=.4)
plt.title("Manga Sales")
plt.xlabel("Month Number")
plt.ylabel("Total Sale")
plt.legend()
plt.show()