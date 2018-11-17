import pandas_datareader.data as pdr
import fix_yahoo_finance as fix
fix.pdr_override()


class GetData:
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end

    # get stock data
    def get_stock_data(self):
        stock_data = pdr.get_data_yahoo(self.ticker, self.start, self.end)
        stock_data.to_csv('IBM_1990-01-01_to_2018-11-15.csv')

    # get twitter data
    # do your code here!

    # get news data
    # do your code here!


if __name__ == "__main__":
    data = GetData("IBM", "1990-01-01", "2018-11-15")
    data.get_stock_data()
