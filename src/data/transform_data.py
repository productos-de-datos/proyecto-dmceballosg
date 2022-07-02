"""
Módulo de transformación de datos en columnas necesarias para analisis
Debe ser ejecutado ya sea desde el directorio actual o desde la raiz del proyecto
"""

import sys
import subprocess
import pandas as pd


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openpyxl'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'xlrd'])
    number_skips = {
        1995: 3, 1996: 3, 1997: 3, 1998: 3, 1999: 3, 2000: 2,
        2001: 2, 2002: 2, 2003: 2, 2004: 2, 2005: 2, 2006: 2,
        2007: 2, 2008: 2, 2009: 2, 2010: 2, 2011: 2, 2012: 2,
        2013: 2, 2014: 2, 2015: 2, 2016: 2, 2017: 2, 2018: 0,
        2019: 0, 2020: 0, 2021: 0, 2022: 0
    }

    for year in range(1995, 2022):
        extention = '.xlsx' if year not in (2016, 2017) else '.xls'
        route_try = True
        try:
            read_file = pd.read_excel(
                "./data_lake/landing/" + str(year) + extention, skiprows=number_skips[year])
        except FileNotFoundError:
            route_try = False
            read_file = pd.read_excel(
                "../../data_lake/landing/" + str(year) + extention, skiprows=number_skips[year])
        read_file = read_file.loc[:, read_file.columns.notna()]
        if 'Version' in read_file.columns:
            read_file = read_file.drop(columns=['Version'])
        if 'Unnamed: 26' in read_file.columns:
            read_file = read_file.drop(columns=['Unnamed: 26'])
        route = "./data_lake/raw/" if route_try else "../../data_lake/raw/"
        read_file.to_csv(route + str(year) + ".csv", index=False)


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
