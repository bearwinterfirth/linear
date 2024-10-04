import pandas as pd
import matplotlib.pyplot as plt

# path="unlabelled_data.csv"

data=pd.read_csv("unlabelled_data.csv", header=None)

print(data)
data.plot(kind="scatter", x=0, y=1)


plt.grid()
plt.show()




