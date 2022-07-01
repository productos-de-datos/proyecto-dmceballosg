import pandas as pd
from holidays_co import is_holiday_date

def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    df = pd.read_csv("./data_lake/business/precios-diarios.csv")
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["ano"] = df["fecha"].dt.year
    df["mes"] = df["fecha"].dt.month
    df["dia"] = df["fecha"].dt.day
    df["tipo_dia"] = df["fecha"].dt.dayofweek 
    df["festivo"] = df["fecha"].map(lambda x: 1 if is_holiday_date(x) else 0)
    df["fin_semana"] = df["fecha"].map(lambda x:  len(pd.bdate_range(x,x)))

    df.to_csv("./data_lake/business/features/precios_diarios.csv", index=False)


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
