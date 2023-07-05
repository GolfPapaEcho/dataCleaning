#  %%
import pandas as pd
def read():
    return pd.read_csv('/home/michael/CSF/dataCleaning/jc230316-17Q0Hz300200.csv')

df = read()

# %%
df.head
# %%

columnsdf = ['h/cm','Midpoint Time/m', 'Q/(uL/min) h=200mm', 'Q/(uL/min)h=300 mm']

df = df.drop(columnsdf[1], axis=1)


# %%
df = df.dropna(axis=0)

# %%
header0 = [columnsdf[0], 'Mass/g']
df.to_csv('/home/michael/CSF/CSF/FigurePrepFiles/mh2301120Hertz.csv',header=False,index=False)


# %%
df3 = read()
# %%
df3.head

# %%
df3 = df3.drop(columnsdf[1], axis=1) # do you mean to drop on df or df3?
df3 = df3.dropna(axis=0)
# %%
header1 = [columnsdf[0], 'Mass/g']
df3.to_csv('/home/michael/CSF/CSF/FigurePrepFiles/mh2301123Hertz.csv',header=False,index=False)
# %%
