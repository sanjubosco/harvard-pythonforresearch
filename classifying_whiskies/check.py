import pandas as pd 
import matplotlib.pyplot as plt
import os

local_path = os.path.dirname(os.path.realpath(__file__))
regions = pd.read_csv(os.path.join(local_path,"regions.csv"), skiprows=1, header = None, names = ["Region"])
whiskies = pd.read_csv(os.path.join(local_path,"whiskies.csv"))
flavors = whiskies.iloc[:,2:14]
print (regions.head())
print(whiskies.head())
print (flavors.head())

corr_whiskey = pd.DataFrame.corr(flavors)
plt.figure(figsize=(10,10))
plt.pcolor(corr_whiskey)
plt.axis("tight")
plt.colorbar()
plt.show()
