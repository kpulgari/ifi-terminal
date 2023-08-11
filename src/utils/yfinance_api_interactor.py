import yfinance as yf


# The YFinanceAPI class provides methods to retrieve high, low, and historical data for a given stock
# using the yfinance library.
class YFinanceAPI:
    def __init__(self, stock: str) -> None:
        """
        The function initializes an object with a stock ticker and retrieves fast information about the
        stock using the yf.Ticker class.

        :param stock: The `stock` parameter is a string that represents the stock symbol or ticker of a
        company. It is used to initialize the `Ticker` object from the `yf` module
        :type stock: str
        """
        self.ticker = yf.Ticker(stock)
        self.fast_info = self.ticker.fast_info

    def get_high(self) -> float:
        """
        The function `get_high` returns the value of the 'dayHigh' key from the `fast_info` dictionary.
        :return: the value of the 'dayHigh' key from the 'fast_info' dictionary.
        """
        return self.fast_info['dayHigh']

    def get_low(self) -> float:
        """
        The function `get_low` returns the value of the 'dayLow' key from the `fast_info` dictionary.
        :return: the value of the 'dayLow' key from the 'fast_info' dictionary.
        """
        return self.fast_info['dayLow']

    def get_history(self, period):
        """
        The function "get_history" returns the historical data for a given period.

        :param period: The period parameter is used to specify the time period for which you want to
        retrieve the historical data. It can be specified in different formats such as '1d' for daily, '1mo'
        for monthly, '1y' for yearly, etc
        :return: the historical data for a given period.
        """
        return self.ticker.history(period)


if __name__ == "__main__":
    print("Executing yfinance_api_interactor.py")
    yfinance_api = YFinanceAPI("AMZN")
