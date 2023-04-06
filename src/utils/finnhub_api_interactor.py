import finnhub

if __name__ == "__main__":
    from secrets import FINNHUB_API_KEY as API_KEY


class FinnhubAPI:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.finnhub_client = finnhub.Client(api_key=self.api_key)

    def get_quote(self, stock: str) -> dict:
        return self.finnhub_client.quote(stock)
    
    # Subsequent functions can be added later as and when we need something


if __name__ == "__main__":
    print("Executing finnhub_api_interactor.py")
    finhub_api = FinnhubAPI(API_KEY)
    print(type(finhub_api.get_quote('AAPL')))
    print('******')
    print(finhub_api.get_quote('AAPL'))