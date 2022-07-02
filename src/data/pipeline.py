"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.
"""
import luigi
from create_data_lake import create_data_lake
from ingest_data import ingest_data
from transform_data import transform_data
from clean_data import clean_data
from compute_daily_prices import compute_daily_prices
from compute_monthly_prices import compute_monthly_prices

class CreateStructure(luigi.Task):
    """
    Ejecuta la tarea de crear la estructura
    """
    def output(self):
        return []

    def run(self):
        create_data_lake()

class IngestData(luigi.Task):
    """
    Ejecuta la tarea de recuperar la data desde un archivo externo
    """
    def output(self):
        return []

    def run(self):
        ingest_data()

class TransformData(luigi.Task):
    """
    Ejecuta la tarea de transformar la data
    y consolidarla en un unico archivo
    """
    def output(self):
        return []

    def run(self):
        transform_data()

class CleanData(luigi.Task):
    """
    Ejecuta la tarea de limpiar la data y
    dar una estrucutra adecuada
    """
    def output(self):
        return []

    def run(self):
        clean_data()

class ComputeDailyPrices(luigi.Task):
    """
    Ejecuta la tarea de consolidar los precios a nivel diario
    """
    def output(self):
        return []

    def run(self):
        compute_daily_prices()

class ComputeMonthlyPrices(luigi.Task):
    """
    Ejecuta la tarea de consolidar los precios a nivel mensual
    """
    def output(self):
        return []

    def run(self):
        compute_monthly_prices()


def pipeline():
    """
        llama al pipeline
    """
    luigi.build([CreateStructure(), IngestData(), TransformData(), CleanData(), ComputeDailyPrices(), ComputeMonthlyPrices() ],  local_scheduler=True)

if __name__ == "__main__":
    import doctest
    pipeline()
    doctest.testmod()
