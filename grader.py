#
# Evaluador
# ---------------------------------------------------------------------------------------
#
# test_01: pylint
# test_02: pytest
# test_03: doctest
#
import os
import sys


def test_01():
    """Califica la creación del data lake"""
    os.system("rm -rf data_lake")
    os.system("make create_data_lake")
    assert os.path.isdir("data_lake/business") is True
    assert os.path.isdir("data_lake/business/reports/figures") is True
    assert os.path.isdir("data_lake/business/features") is True
    assert os.path.isdir("data_lake/business/forecasts") is True
    assert os.path.isdir("data_lake/cleansed") is True
    assert os.path.isdir("data_lake/landing") is True
    assert os.path.isdir("data_lake/raw") is True


def test_02():
    """Califica la ingestión de datos"""
    os.system("make ingest_data")
    assert os.path.isfile("data_lake/landing/1995.xlsx") is True
    assert os.path.isfile("data_lake/landing/1996.xlsx") is True
    assert os.path.isfile("data_lake/landing/1997.xlsx") is True
    assert os.path.isfile("data_lake/landing/1998.xlsx") is True
    assert os.path.isfile("data_lake/landing/1999.xlsx") is True
    assert os.path.isfile("data_lake/landing/2000.xlsx") is True
    assert os.path.isfile("data_lake/landing/2001.xlsx") is True
    assert os.path.isfile("data_lake/landing/2002.xlsx") is True
    assert os.path.isfile("data_lake/landing/2003.xlsx") is True
    assert os.path.isfile("data_lake/landing/2004.xlsx") is True
    assert os.path.isfile("data_lake/landing/2005.xlsx") is True
    assert os.path.isfile("data_lake/landing/2006.xlsx") is True
    assert os.path.isfile("data_lake/landing/2007.xlsx") is True
    assert os.path.isfile("data_lake/landing/2008.xlsx") is True
    assert os.path.isfile("data_lake/landing/2009.xlsx") is True
    assert os.path.isfile("data_lake/landing/2010.xlsx") is True
    assert os.path.isfile("data_lake/landing/2011.xlsx") is True
    assert os.path.isfile("data_lake/landing/2012.xlsx") is True
    assert os.path.isfile("data_lake/landing/2013.xlsx") is True
    assert os.path.isfile("data_lake/landing/2014.xlsx") is True
    assert os.path.isfile("data_lake/landing/2015.xlsx") is True
    assert os.path.isfile("data_lake/landing/2016.xls") is True
    assert os.path.isfile("data_lake/landing/2017.xls") is True
    assert os.path.isfile("data_lake/landing/2018.xlsx") is True
    assert os.path.isfile("data_lake/landing/2019.xlsx") is True
    assert os.path.isfile("data_lake/landing/2020.xlsx") is True
    assert os.path.isfile("data_lake/landing/2021.xlsx") is True


def test_03():
    """Califica la transformación de datos de excel a csv"""
    os.system("make transform_data")
    assert os.path.isfile("data_lake/raw/1995.csv") is True
    assert os.path.isfile("data_lake/raw/1996.csv") is True
    assert os.path.isfile("data_lake/raw/1997.csv") is True
    assert os.path.isfile("data_lake/raw/1998.csv") is True
    assert os.path.isfile("data_lake/raw/1999.csv") is True
    assert os.path.isfile("data_lake/raw/2000.csv") is True
    assert os.path.isfile("data_lake/raw/2001.csv") is True
    assert os.path.isfile("data_lake/raw/2002.csv") is True
    assert os.path.isfile("data_lake/raw/2003.csv") is True
    assert os.path.isfile("data_lake/raw/2004.csv") is True
    assert os.path.isfile("data_lake/raw/2005.csv") is True
    assert os.path.isfile("data_lake/raw/2006.csv") is True
    assert os.path.isfile("data_lake/raw/2007.csv") is True
    assert os.path.isfile("data_lake/raw/2008.csv") is True
    assert os.path.isfile("data_lake/raw/2009.csv") is True
    assert os.path.isfile("data_lake/raw/2010.csv") is True
    assert os.path.isfile("data_lake/raw/2011.csv") is True
    assert os.path.isfile("data_lake/raw/2012.csv") is True
    assert os.path.isfile("data_lake/raw/2013.csv") is True
    assert os.path.isfile("data_lake/raw/2014.csv") is True
    assert os.path.isfile("data_lake/raw/2015.csv") is True
    assert os.path.isfile("data_lake/raw/2016.csv") is True
    assert os.path.isfile("data_lake/raw/2017.csv") is True
    assert os.path.isfile("data_lake/raw/2018.csv") is True
    assert os.path.isfile("data_lake/raw/2019.csv") is True
    assert os.path.isfile("data_lake/raw/2020.csv") is True
    assert os.path.isfile("data_lake/raw/2021.csv") is True


def test_04():
    """Califica la creacion de la tabla de precios diarios"""
    os.system("make clean_data")
    assert os.path.isfile("data_lake/cleansed/precios-horarios.csv") is True


def test_05():
    """Computa los precios promedios diarios"""
    os.system("make compute_daily_prices")
    assert os.path.isfile("data_lake/business/precios-diarios.csv") is True


def test_06():
    """Computa los precios promedios mensuales"""
    os.system("make compute_monthly_prices")
    assert os.path.isfile("data_lake/business/precios-mensuales.csv") is True


def test_07():
    """Evalua el pipeline"""
    os.system("make pipeline")
    assert os.path.isfile("data_lake/business/precios-diarios.csv") is True
    assert os.path.isfile("data_lake/business/precios-mensuales.csv") is True


def test_08():
    """Evalua figura precios diarios"""
    assert os.path.isfile("data_lake/business/reports/figures/daily_prices.png") is True


def test_09():
    """Evalua figura precios diarios"""
    assert (
        os.path.isfile("data_lake/business/reports/figures/monthly_prices.png") is True
    )


def test_10():
    """Evalua la creación de características para modelos"""
    assert os.path.isfile("data_lake/business/features/precios_diarios.csv") is True


def test_11():
    """Modelo creado"""
    assert os.path.isfile("modeles/precios-diarios.pkl") is True


def test_12():
    """Pronosticos"""
    assert os.path.isfile("data_lake/business/forecasts/precios-diarios.csv") is True


test = {
    "01": test_01,
    "02": test_02,
    "03": test_03,
    "04": test_04,
    "05": test_05,
    "06": test_06,
    "07": test_07,
    "08": test_08,
    "09": test_09,
    "10": test_10,
    "11": test_11,
    "12": test_12,
}[sys.argv[1]]

test()
