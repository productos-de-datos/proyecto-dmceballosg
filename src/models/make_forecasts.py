import pandas as pd
import joblib
import os
import math
def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    
    df_feature_train = pd.read_csv('./data_lake/business/forecasts/dataToForecast.csv')
    df_prices = df_feature_train.copy()
    df_feature_train  = df_feature_train.drop(columns = ['Unnamed: 0', 'y'])

    parent_dir = "src/models/precios-diarios.pkl"
    cwd = os.getcwd()
    path_parent_dir = os.path.join(cwd, parent_dir)
    model = joblib.load(path_parent_dir)
    data_result = model.predict(df_feature_train)
    df_feature_train["precio_promedio_pronostico"] = data_result
    df_feature_train = df_feature_train.drop(columns = ['tipo_dia','festivo', 'fin_semana'])
    df_feature_train["fecha"] = df_feature_train.apply(lambda x : str(math.floor(x.ano)) + "-" + str(add_digit(x.mes)) + "-" + str(add_digit(x.dia)), axis=1)  
    df_feature_train = df_feature_train.drop(columns = ['ano','mes', 'dia'])
    df_feature_train["precio_promedio_real"] = df_prices["y"]
    df_feature_train = df_feature_train[["fecha", "precio_promedio_real", "precio_promedio_pronostico"]]
    df_feature_train.to_csv('./data_lake/business/forecasts/precios-diarios.csv', index=False)
    
def add_digit(data):
    return  '0' + str(math.floor(data)) if len(str(math.floor(data))) < 2 else str(math.floor(data))


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
