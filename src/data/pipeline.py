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
import os
from create_data_lake import create_data_lake
from ingest_data import ingest_data
from transform_data import transform_data
from clean_data import clean_data
from compute_daily_prices import compute_daily_prices
from compute_monthly_prices import compute_monthly_prices


class createStructure(luigi.Task):
    def output(self):
        return []

    def run(self):
        create_data_lake()

class ingestData(luigi.Task):
    def output(self):
        return []

    def run(self):
        ingest_data()

class transformData(luigi.Task):
    def output(self):
        return []

    def run(self):
        transform_data()

class cleanData(luigi.Task):
    def output(self):
        return []

    def run(self):
        clean_data()

class computeDailyPrices(luigi.Task):
    def output(self):
        return []

    def run(self):
        compute_daily_prices()

class computeMonthlyPrices(luigi.Task):
    def output(self):
        return []

    def run(self):
        compute_monthly_prices()


def pipeline():
    luigi.build([createStructure(), ingestData(), transformData(), cleanData(), computeDailyPrices(), computeMonthlyPrices() ],  local_scheduler=True)

if __name__ == "__main__":
    import doctest
    pipeline()
    doctest.testmod()