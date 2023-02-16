#  %%
import pandas as pd
def read():
    return pd.read_csv('/home/michael/CSF/CSF/FigurePrepFiles/mh230112forPandas230206.csv')

df = read()

# %%
df.head
# %%

columnsdf = ['#Time to Measuement/s', 'Mass/g (0Hz)', 'Mass/g(3 Hz)']

df = df.drop(columnsdf[2], axis=1)


# %%
df = df.dropna(axis=0)

# %%
header0 = [columnsdf[0], 'Mass/g']
df.to_csv('/home/michael/CSF/CSF/FigurePrepFiles/mh2301120Hertz.csv',header=header0,index=False)


# %%
df3 = read()
# %%
df3.head

# %%
df3 = df3.drop(columnsdf[1], axis=1) # do you mean to drop on df or df3?
df3 = df3.dropna(axis=0)
# %%
header1 = [columnsdf[0], 'Mass/g']
df3.to_csv('/home/michael/CSF/CSF/FigurePrepFiles/mh2301123Hertz.csv',header=header1,index=False)
# %%
