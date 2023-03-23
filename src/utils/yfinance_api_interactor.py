import yfinance as yf

class YFinanceAPI:
    def __init__(self, stock: str) -> None:
        self.ticker = yf.Ticker(stock)

    def get_recommendations(self) -> list:
        return self.ticker.recommendations
    
    # add more functions

# rename secrets.py
if __name__ == "__main__":
    print("Executing yfinance_api_interactor.py")
    yfinance_api = YFinanceAPI("AMZN")
    print(yfinance_api.get_recommendations())

