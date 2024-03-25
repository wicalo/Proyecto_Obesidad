import pandas as pd
from sklearn.inspection import permutation_importance

def redondear_variables(df, variables):
    for var in variables:
        df[var] = df[var].round().astype(int)
        df=pd.DataFrame(df)
    return df


def importancia(flujo,X,Y ):
    importancia_modelo = permutation_importance(flujo,X,Y, n_repeats=10, random_state=0)
    ordenado = importancia_modelo.importances_mean.argsort()
    importancias = pd.DataFrame(
    importancia_modelo.importances[ordenado].T,
    columns=X.columns[ordenado])
   
    return importancias