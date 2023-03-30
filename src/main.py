from utils.yfinance_api_interactor import YFinanceAPI
# from utils.reddit_api_interactor import RedditAPI
# from utils.finnhub_api_interactor import FinnhubAPI

import rich
from rich.console import Console
from rich.table import Table


if __name__ == "__main__":
    table = Table(title="Testing")
    table.add_column("Stock", style="cyan")
    table.add_column("Day High", style="green")
    table.add_column("Day Low", style="red")

    yfinance_api = YFinanceAPI("AMZN")
    table.add_row("AMZN", str(yfinance_api.get_high()), str(yfinance_api.get_low()))

    console = Console()
    console.print(table)
