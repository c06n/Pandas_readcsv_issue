# %%
import pandas as pd
import numpy as np

df = pd.DataFrame({'approach': np.r_[[np.nan]*2000,
                              np.repeat('True', 100),
                              [np.nan]*2000,
                              np.repeat('True', 100),
                              [np.nan]*2000]})
df.to_csv('synthetic_data.csv', sep=';', decimal=',', index=False)
df = pd.read_csv('synthetic_data.csv', 
                 na_values='',
                 sep=';',
                #  engine='python',
                 decimal=',',
                 dtype={'approach': 'float'})
df

