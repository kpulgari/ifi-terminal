from utils.yfinance_api_interactor import YFinanceAPI
from utils.reddit_api_interactor import RedditAPI
from utils.finnhub_api_interactor import FinnhubAPI

from rich.console import Console
from rich.table import Table
from rich.color import Color
from rich.style import Style
from rich.live import Live
from rich.table import Table

from utils.secrets import REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD
from utils.secrets import FINNHUB_API_KEY as API_KEY

import random
import time


if __name__ == "__main__":
    selection = input("Select [Y] for yfinance or [R] for reddit: ").upper()

    if selection == "Y":
        yfinance_api_sample = YFinanceAPI("APPL")
        fast_info_choices = [choice for choice in yfinance_api_sample.fast_info]

        choices = ""
        count = 1
        
        for choice in fast_info_choices:
            choices += f"{count}. {choice}\n"
            count += 1

        user_choice_selection = input(f"{choices}Please enter a comma-separated list to select filters: ").replace(" ", "")
        selection_arr = user_choice_selection.split(",")

        colorMapping = {
            "dayHigh": "green",
            "dayLow": "red",
            "exchange": "blue",
            "fiftyDayAverage": "purple"
        }


        stock_cache = []

        while True:
            stock = input("Enter stock: ").upper()

            if stock == "BREAK":
                break
            try:
                try: 
                    if stock in stock_cache:
                        raise ValueError()
                    
                    stock_cache.append(stock)
                except:
                    print(f"{stock} has already been added!")

            except Exception as e:
                print("Invalid stock!")



        def generate_table() -> Table:
            column_cache = []
            """Make a new table."""
            table = Table(title="YFinance Testing")
            table.add_column("STOCK", style="bold cyan")
            for selection in selection_arr:
                column = fast_info_choices[int(selection) - 1]
                

                style = Style(color=Color.from_rgb(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
                style = colorMapping.get(column, style)
                table.add_column(column.upper(), style=style, justify="center")  
                column_cache.append(column) 

            for stock in stock_cache:
                yfinance_api = YFinanceAPI(stock)
                row_values = [stock] + [str(yfinance_api.fast_info[column]) for column in column_cache]
                table.add_row(*row_values)
            return table

        
        with Live(generate_table(), refresh_per_second=4) as live:
            for _ in range(5):
                time.sleep(5)
                live.update(generate_table())
                print("updated")

    elif selection == "R":
        reddit_api = RedditAPI(REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD)

        subreddit = input("Enter a subreddit: ")
        post_limit = int(input("Enter the hot post limit: "))
        post_arr = reddit_api.get_hot_posts(subreddit, post_limit)

        comment_limit = int(input("Enter the comment limit: "))

        table = Table(title="Reddit Testing")
        table.add_column("Post")
        table.add_column("Comments")

        for post in post_arr:
            comment_arr = reddit_api.get_post_top_comments(post, comment_limit)
            comment_str = ""

            for comment in comment_arr:
                comment_str += comment.body + "\n"

            style = Style(color=Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

            table.add_row(post.title, comment_str, style=style)
        
        console = Console()
        console.print(table)

    else:
        print("Invalid selection!")




    
