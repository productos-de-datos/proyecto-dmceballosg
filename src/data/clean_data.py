""" Limpia y transforma los archivos para consolidarlos y posteriormente precesarlos
    Debe ser ejecutado ya sea desde el directorio actual o desde la raiz del proyecto
"""
import pandas as pd

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv,
    cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:
    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    dict_hours = {'0': '00', '1':'01', '2':'02', '3':'03',
     '4': '04', '5':'05', '6':'06', '7':'07', '8':'08', '9': '09'}
    try:
        df_completed = pd.read_csv("./data_lake/raw/1995.csv")
    except FileNotFoundError:
        df_completed = pd.read_csv("../../data_lake/raw/1995.csv")

    df_completed = df_completed.rename(columns=dict_hours)
    df_completed = pd.melt(df_completed, id_vars= ["Fecha"], value_vars = [str(hour) if hour >=10  else '0'+ str(hour) for hour in range(0,24)])
    for i in range(1996,2022):
        route_try = True
        try:
            df_to_clear = pd.read_csv("./data_lake/raw/" + str(i) + ".csv")
        except FileNotFoundError:
            route_try = False
            df_to_clear = pd.read_csv("../../data_lake/raw/" + str(i) + ".csv")
        df_to_clear = df_to_clear.rename(columns=dict_hours)
        df_to_clear = pd.melt(df_to_clear, id_vars= ["Fecha"], value_vars = [str(hour) if hour >=10  else '0'+ str(hour) for hour in range(0,24)])
        df_completed = pd.concat([df_completed,df_to_clear])

    df_completed =  df_completed.rename(columns={"Fecha": "fecha", "variable": "hora", "value": "precio"})
    route = "./data_lake/cleansed/precios-horarios.csv" if route_try else "../../data_lake/cleansed/precios-horarios.csv"
    df_completed.to_csv(route, index=False)

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
