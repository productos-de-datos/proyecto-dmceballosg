import pandas as pd
def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    read_file = pd.read_excel("./data_lake/landing/1995.xlsx", engine='openpyxl')   

    
    print(read_file.head(5))


if __name__ == "__main__":
    import doctest
    print("estoy en el punto3")
    transform_data()
    doctest.testmod()
