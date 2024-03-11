import pandas as pd

def redondear_variables(df, variables):
    for var in variables:
        df[var] = df[var].round().astype(int)
        df=pd.DataFrame(df)
    return df
