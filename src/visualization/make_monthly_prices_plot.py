"""
Crea grafico de lineas que representa los precios promedios mensuales.
"""
import pandas as pd
import matplotlib.pyplot as plt
def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/monthly_prices.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.

    """
    df_monthly_prices = pd.read_csv("./data_lake/business/precios-mensuales.csv")
    plt.plot(df_monthly_prices["fecha"], df_monthly_prices["precio"])
    plt.savefig('./data_lake/business/reports/figures/monthly_prices.png')


if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()
