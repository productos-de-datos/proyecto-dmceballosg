import os
def create_data_lake():
    """Cree el data lake con sus capas.
    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:
    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
    """
    parent_dir = "data_lake"
    os.chdir("../../")
    cwd = os.getcwd()
    path_data_lake = os.path.join(cwd, parent_dir)

    if os.path.isdir(path_data_lake):
        os.system("rm -rf "+ parent_dir)

    os.makedirs(path_data_lake)
    os.makedirs(path_data_lake + "/landing")
    os.makedirs(path_data_lake + "/raw")
    os.makedirs(path_data_lake + "/cleansed")
    os.makedirs(path_data_lake + "/business")

    os.makedirs(path_data_lake + "/business/reports")
    os.makedirs(path_data_lake + "/business/reports/figures")
    os.makedirs(path_data_lake + "/business/features")
    os.makedirs(path_data_lake + "/business/forecasts")

if __name__ == "__main__":
    import doctest
    create_data_lake()
    doctest.testmod()
