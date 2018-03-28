import numpy as np
import pandas as pd

data = pd.read_csv('acs2015_census_tract_data.csv')

data = data.groupby('State', as_index=False).sum()


import matplotlib.pyplot as plt

import seaborn as sns

data = data.sort_values('TotalPop')

fig, ax = plt.subplots(figsize=(14,4))
fig = sns.barplot(x = data ['State'], y = data['TotalPop'], data=data)
fig.axis(ymin=0, ymax=40000000)
plt.xticks(rotation=90)
plt.show()
