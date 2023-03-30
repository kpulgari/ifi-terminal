from utils.yfinance_api_interactor import YFinanceAPI
# from utils.reddit_api_interactor import RedditAPI
# from utils.finnhub_api_interactor import FinnhubAPI

from rich.console import Console
from rich.table import Table


if __name__ == "__main__":
    table = Table(title="Testing")
    table.add_column("Stock", style="cyan")
    table.add_column("Day High", style="green")
    table.add_column("Day Low", style="red")

    while True:
        stock = input("Enter stock: ")

        if stock == "break":
            break

        try:
            yfinance_api = YFinanceAPI(stock)
            table.add_row(stock.upper(), str(yfinance_api.get_high()), str(yfinance_api.get_low()))
        except:
            print("Invalid stock!")
    
    console = Console()
    console.print(table)
    
