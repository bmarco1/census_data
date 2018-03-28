import numpy as np
import pandas as pd

data = pd.read_csv('acs2015_census_tract_data.csv')

data = data.groupby('State', as_index=False).sum()


import matplotlib.pyplot as plt

import seaborn as sns

data = data.sort_values('TotalPop')


sns.distplot(data['TotalPop'])
plt.show()
