"""
Crea nuevas caracteristicas para predecir el precio diario de electricidad.
Las caracteristicas agregadas son: dia, mes, ano, tipo_dia, festivo, fin_semana
"""
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
    data_to_predict = pd.read_csv("./data_lake/business/precios-diarios.csv")
    data_to_predict["fecha"] = pd.to_datetime(data_to_predict["fecha"])
    data_to_predict["ano"] = data_to_predict["fecha"].dt.year
    data_to_predict["mes"] = data_to_predict["fecha"].dt.month
    data_to_predict["dia"] = data_to_predict["fecha"].dt.day
    data_to_predict["tipo_dia"] = data_to_predict["fecha"].dt.dayofweek
    data_to_predict["festivo"] = data_to_predict["fecha"].map(lambda x: 1 if is_holiday_date(x) else 0)
    data_to_predict["fin_semana"] = data_to_predict["fecha"].map(lambda x:  len(pd.bdate_range(x,x)))

    data_to_predict.to_csv("./data_lake/business/features/precios_diarios.csv", index=False)


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
