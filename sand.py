import pandas as pd
import matplotlib.pyplot as plt

# path="unlabelled_data.csv"

data=pd.read_csv("unlabelled_data.csv", header=None)

print(data)
data.plot(kind="scatter", x=0, y=1)


plt.grid()
plt.show()


# with open(path2, "w", newline='') as labelled:          # https://discuss.python.org/t/writing-to-csv-files-unwanted-blank-row-in-file/28391
#     write=csv.writer(labelled)
#     write.writerows(data_list)                          # https://www.geeksforgeeks.org/writing-csv-files-in-python/

