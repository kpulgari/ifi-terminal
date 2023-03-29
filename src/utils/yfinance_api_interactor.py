import yfinance as yf

class YFinanceAPI:
    def __init__(self, stock: str) -> None:
        self.ticker = yf.Ticker(stock)
        self.fast_info = self.ticker.fast_info
    
    def get_high(self) -> float:
        return self.fast_info['dayHigh']
    
    def get_low(self) -> float:
        return self.fast_info['dayLow']

# rename secrets.py
if __name__ == "__main__":
    print("Executing yfinance_api_interactor.py")
    yfinance_api = YFinanceAPI("AMZN")
    print(yfinance_api.get_high(), yfinance_api.get_low())





# # get all stock info (slow)
# msft.info
# # fast access to subset of stock info (opportunistic)
# print(msft.fast_info['dayHigh'])

# # get historical market data
# hist = msft.history(period="1mo")

# # show meta information about the history (requires history() to be called first)
# msft.history_metadata

# # show actions (dividends, splits, capital gains)
# msft.actions
# msft.dividends
# msft.splits
# msft.capital_gains  # only for mutual funds & etfs

# # show share count
# # - accurate time-series count:
# msft.get_shares_full(start="2022-01-01", end=None)

# # show holders
# msft.major_holders
# msft.institutional_holders
# msft.mutualfund_holders

# # show options expirations
# msft.options

# # show news
# msft.news