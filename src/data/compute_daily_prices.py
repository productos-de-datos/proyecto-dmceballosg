""" Crea un achivo con los precios promedios consolidados por dia.
    Debe ser ejecutado ya sea desde el directorio actual o desde la raiz del proyecto
"""
import pandas as pd
def compute_daily_prices():
    """Compute los precios promedios diarios.
    >>> compute_daily_prices()
            fecha    precio
    0  1995-07-20  1.409435
    1  1995-07-21  4.924333
    2  1995-07-22  1.269500
    3  1995-07-23  0.953083
    4  1995-07-24  4.305917

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    route_try = True
    try:
        df_completed = pd.read_csv("./data_lake/cleansed/precios-horarios.csv")
    except FileNotFoundError:
        route_try = False
        df_completed = pd.read_csv("../../data_lake/cleansed/precios-horarios.csv")
    df_completed = df_completed.groupby('fecha', as_index=False).mean()
    df_completed = df_completed[['fecha','precio']]
    route = "./data_lake/business/precios-diarios.csv" if route_try else "../../data_lake/business/precios-diarios.csv"
    df_completed.to_csv(route, index=False)
    print(df_completed.head())

if __name__ == "__main__":
    import doctest

    compute_daily_prices()
    doctest.testmod()
