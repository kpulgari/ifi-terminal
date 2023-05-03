import yfinance as yf

class YFinanceAPI:
    def __init__(self, stock: str) -> None:
        self.ticker = yf.Ticker(stock)
        self.fast_info = self.ticker.fast_info
    
    def get_high(self) -> float:
        return self.fast_info['dayHigh']
    
    def get_low(self) -> float:
        return self.fast_info['dayLow']
    
    def get_history(self, period):
        return self.ticker.history(period)

if __name__ == "__main__":
    print("Executing yfinance_api_interactor.py")
    yfinance_api = YFinanceAPI("AMZN")
    hist = yfinance_api.get_history("1day")
    print(yfinance_api.fast_info['dayLow'])