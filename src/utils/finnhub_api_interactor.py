import finnhub


# The `FinnhubAPI` class is a Python class that provides a method to retrieve stock quotes using the
# Finnhub API.
class FinnhubAPI:
    def __init__(self, api_key: str) -> None:
        """
        The `__init__` function initializes an instance of a class with an API key and creates a Finnhub
        client object.

        :param api_key: The `api_key` parameter is a string that represents the API key required to access
        the Finnhub API. This API key is used to authenticate and authorize the requests made to the Finnhub
        API
        :type api_key: str
        """
        self.api_key = api_key
        self.finnhub_client = finnhub.Client(api_key=self.api_key)

    def get_quote(self, stock: str) -> dict:
        """
        The function `get_quote` takes a stock symbol as input and returns a dictionary containing the quote
        information for that stock.

        :param stock: The stock parameter is a string that represents the stock symbol or ticker symbol of a
        particular company
        :type stock: str
        :return: a dictionary.
        """
        return self.finnhub_client.quote(stock)


if __name__ == "__main__":
    from secrets import FINNHUB_API_KEY as API_KEY
    print("Executing finnhub_api_interactor.py")
    finhub_api = FinnhubAPI(API_KEY)
