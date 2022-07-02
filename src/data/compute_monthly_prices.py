""" Crea un achivo con los precios promedios consolidados por mes y año.
    Debe ser ejecutado ya sea desde el directorio actual o desde la raiz del proyecto
"""
import pandas as pd
def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional
    """
    route_try = True
    try:
        df_completed = pd.read_csv("./data_lake/cleansed/precios-horarios.csv")
    except FileNotFoundError:
        route_try = False
        df_completed = pd.read_csv("../../data_lake/cleansed/precios-horarios.csv")
    df_completed["year-month"] = df_completed["fecha"].map(lambda x: str(x)[0:7])

    df_completed = df_completed.groupby('year-month', as_index=False).mean()
    df_completed = df_completed[['year-month','precio']]
    df_completed = df_completed.rename(columns= {'year-month': 'fecha'})
    df_completed["fecha"] =  df_completed["fecha"].map(lambda x: x + str("-01"))
    route = "./data_lake/business/precios-mensuales.csv" if route_try else "../../data_lake/business/precios-mensuales.csv"
    df_completed.to_csv(route, index=False)

if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
