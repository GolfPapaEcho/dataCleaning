#  %%
import pandas as pd
def read():
    return pd.read_csv('/home/michael/CSF/CSF/FigurePrepFiles/mh230112forPandas230206.csv')

df = read()

# %%
df.head
# %%

columnsdf = ['Time to Measuement/s', 'Mass/g (0Hz)', 'Mass/g(3 Hz)']

df1 = df.drop(columnsdf[2], axis=1, inplace=True)


# %%
df2 = df.dropna(axis=0, inplace=True).reset_index()

# %%
#header = [columnsdf[0], columnsdf[1]]
df2.to_csv('mh2301120Hertz.csv', index=False)


# %%
df3 = read()
df4 = df.drop(columnsdf[1], axis=1, inplace=True)
df5 = df.dropna(axis=0, inplace=True).reset_index()
# %%
#header1 = [columnsdf[0], columnsdf[2]]
df5.to_csv('mh2301123Hertz.csv', index=False)
# %%
