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


def render_yfinance_terminal():
    # Retrieving available stock parameters
    print("Welcome to ifi_terminal's fundamental financial information terminal! We offer a myriad of live stock information as indicated below:")
    yfinance_api_sample = YFinanceAPI("APPL")
    fast_info_choices = []

    for choice in yfinance_api_sample.fast_info:
        try:
            yfinance_api_sample.fast_info[choice]
            fast_info_choices.append(choice)
        except:
            continue

    valid_selection = False
    choices = ""
    count = 1
    
    for choice in fast_info_choices:
        choices += f"{count}. {choice}\n"
        count += 1
    
    time.sleep(1)

    # Validating user selections
    while not valid_selection:
        user_choice_selection = input(f"{choices}Please enter a comma-separated list of integers within the range [1, {count - 1}] to select stock filters: ").replace(" ", "")
        selection_arr = user_choice_selection.split(",")

        try:
            for selection in selection_arr:
                x = int(selection)
                assert x > 0 and x < count
            
            valid_selection = True
        except:
            print(f"Invalid selection! Enter a comma-separated list of integers within the valid range [1, {count - 1}] to select filters.")
            time.sleep(3)

    # Removing duplicate selections
    selection_arr = [*set(selection_arr)]

    # Maps columns to specified colors
    colorMapping = {
        "dayHigh": "green",
        "dayLow": "red",
        "exchange": "blue",
        "fiftyDayAverage": "purple"
    }

    # Stock validation - checking if valid stock and if already in cache
    stock_cache = []

    while True:
        stock = input("Enter stock (enter 'break' to stop) or enter 'default' to use our watchlist: ").upper()
        if stock == "BREAK":
            break
        elif stock == "DEFAULT":
            stock = "AAPL,MSFT,GOOG,AMZN,TSLA,JPM,NVDA,META,UNH,DIS"
            stock_cache = stock.split(",")
            break
        try:
            yfinance_api = YFinanceAPI(stock)
            yfinance_api.get_high()

            try: 
                if stock in stock_cache:
                    raise ValueError()
                stock_cache.append(stock)
            except:
                print(f"{stock} has already been added!")

        except Exception as e:
            print("Invalid stock!")

    # Generates new table for live stock updates
    def generate_table() -> Table:
        column_cache = []

        table = Table(title="Stock Data")
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
    
    # Asking user for time constraints
    selected_time = False
    while not selected_time:
        try:
            frequency = int(input("Please enter how often (seconds) to update table: "))
            duration = int(input("Please enter the lifespan (seconds) of the table: "))
            assert frequency > 0 and duration > 0

            selected_time = True
        except:
            print("Please enter positive integers only.")
    
    # Updates table with live data
    with Live(generate_table(), refresh_per_second=4) as live:
        for _ in range(duration // frequency):
            time.sleep(frequency)
            live.update(generate_table())


def render_reddit_terminal():
    # User login
    reddit_api = RedditAPI(REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD)

    # Asking user for input
    subreddit = input("Enter a subreddit: ")
    post_limit = int(input("Enter the hot post limit: "))
    post_arr = reddit_api.get_hot_posts(subreddit, post_limit)

    comment_limit = int(input("Enter the comment limit: "))

    table = Table(title="Reddit Testing")
    table.add_column("Post")
    table.add_column("Comments")

    # Generating table
    for post in post_arr:
        comment_arr = reddit_api.get_post_top_comments(post, comment_limit)
        comment_str = ""

        for comment in comment_arr:
            comment_str += comment.body + "\n"

        style = Style(color=Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        table.add_row(post.title, comment_str, style=style)
    
    console = Console()
    console.print(table)


def render_finnhub_terminal(choice, default_terminal=False):
    api_obj = FinnhubAPI(API_KEY)

    stock_cache = []

    while True:
        if default_terminal:
            stock = "AAPL,MSFT,GOOG,AMZN,TSLA,JPM,NVDA,META,UNH,DIS"
            stock_cache = stock.split(",")
            break
        stock = input("Enter stock (enter 'break' to stop) or enter 'default' to use our watchlist, invalid entries will be ignored: ").upper()
        if stock == "BREAK":
            break
        elif stock == "DEFAULT":
            stock = "AAPL,MSFT,GOOG,AMZN,TSLA,JPM,NVDA,META,UNH,DIS"
            stock_cache = stock.split(",")
            break
        try:
            api_obj.get_quote(stock)


            try: 
                if stock in stock_cache:
                    raise ValueError()
                stock_cache.append(stock)
            except:
                print(f"{stock} has already been added!")

        except Exception as e:
            print("Invalid stock!")


    if choice == "1":
        table = Table(title="Decision Helper - Bot 1")
        table.add_column("Stock")
        table.add_column("Change")
        table.add_column("Percent Change")
        for stock in stock_cache:
            status = api_obj.get_quote(stock)
            percent_change = status["dp"] * 100
            if percent_change > 0:
                table.add_row(stock, str(status["d"]), str(percent_change), style="green")
            else:
                table.add_row(stock, str(status["d"]), str(percent_change), style="red")
    elif choice == "2":
        table = Table(title="Decision Helper - Bot 2")
        table.add_column("Stock")
        table.add_column("Bull/Bear Indicator")
        table.add_column("Opening Price")
        table.add_column("Current Price")
        for stock in stock_cache:
            status = api_obj.get_quote(stock)
            if status["c"] > status["o"]:
                table.add_row(stock, "Bull", str(status["o"]), str(status["c"]), style="green")
            else:
                table.add_row(stock, "Bear", str(status["o"]), str(status["c"]), style="red")
    elif choice == "3":
        table = Table(title="Decision Helper - Bot 3")
        table.add_column("Stock")
        table.add_column("Trading Gap - sentiment change in stock and hence gap in opening and closing price")
        table.add_column("Opening Price")
        table.add_column("Previous Closing Price")
        table.add_column("Gap")
        for stock in stock_cache:
            status = api_obj.get_quote(stock)
            if status["o"] > status["pc"]:
                table.add_row(stock, "Trading Gap with positive sentiment", str(status["o"]), str(status["pc"]), str(status["o"] - status["pc"]), style="green")
            else:
                table.add_row(stock, "Trading Gap with pegative sentiment", str(status["o"]), str(status["pc"]), str(status["o"] - status["pc"]), style="red")
    elif choice == "4":
        table = Table(title="Decision Helper - Bot 4")
        table.add_column("Stock")
        table.add_column("Trend Details")
        table.add_column("Low")
        table.add_column("Previous close")
        table.add_column("Price change")
        for stock in stock_cache:
            status = api_obj.get_quote(stock)
            if status["l"] > status["pc"]:
                table.add_row(stock, "Low of the day is higher than the closing price of the previous day", str(status['l']), str(status['pc']), str(status["l"] - status["pc"]), style="green")

            else:
                table.add_row(stock, "Low of the day is lower than the closing price of the previous day", str(status['l']), str(status['pc']), str(status["l"] - status["pc"]), style="red")
    else:
        print("Invalid choice! Exiting decision helper!")

    return table

def render_default_terminal():
    # Retrieving parameters
    yfinance_api_sample = YFinanceAPI("APPL")
    fast_info_choices = []
    selection_arr = [2, 3, 5, 16, 17, 18]

    for choice in yfinance_api_sample.fast_info:
        try:
            yfinance_api_sample.fast_info[choice]
            fast_info_choices.append(choice)
        except:
            continue
    
    stock = "AAPL,MSFT,GOOG,AMZN,TSLA,JPM,NVDA,META,UNH,DIS"
    stock_cache = stock.split(",")

    # Generating table
    def generate_table_main() -> Table:
        column_cache = []

        table = Table(title="Stock Data")
        table.add_column("STOCK", style="bold cyan")

        for selection in selection_arr:
            column = fast_info_choices[int(selection) - 1]
            
            style = Style(color=Color.from_rgb(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))

            table.add_column(column.upper(), style=style, justify="center")  
            column_cache.append(column) 

        for stock in stock_cache:
            yfinance_api = YFinanceAPI(stock)
            row_values = [stock] + [str(yfinance_api.fast_info[column]) for column in column_cache]
            table.add_row(*row_values)

        return table
    
    # Time constraints
    frequency = 3
    duration = 300

    # Retrieving bot tables
    t1 = render_finnhub_terminal("1", True)
    t2 = render_finnhub_terminal("2", True)
    t3 = render_finnhub_terminal("3", True)
    t4 = render_finnhub_terminal("4", True)

    # Printing bot tables
    console = Console()
    console.print(t1)
    console.print(t2)
    console.print(t3)
    console.print(t4)    
    
    # Updates table with live data
    with Live(generate_table_main(), refresh_per_second=4) as live:
        for _ in range(duration // frequency):
            time.sleep(frequency)
            live.update(generate_table_main())


if __name__ == "__main__":
    while True:
        try:
            selection = input("Select: \n [D] for default ifi_terminal display \n [Y] for <yfinance> (traditional financial information) \n [R] for <reddit> data \n [F] for <finnhub> (trend analysis bots) \nPress any other key to exit application: ").upper()

            if selection == "D":
                render_default_terminal()
            
            elif selection == "Y":
                render_yfinance_terminal()

            elif selection == "R":
                render_reddit_terminal()

            elif selection == "F":
                print("Welcome to ifi_terminal's decision helper! We currently offer 4 trend analyses:")
                print("1. Bot 1: Display percent change for select stocks")
                print("2. Bot 2: Bull/Bear indicator chart")
                print("3. Bot 3: Trading gap identification - fundamental for sentiment analysis")
                print("4. Bot 4: Optimistic Trend Check: Is low of the day is higher than the closing price of the previous day?")
                choice = input("Please enter the number of the bot you would like to view: ")

                console = Console()
                table = render_finnhub_terminal(choice, False)
                console.print(table)

            else:
                print("Exiting Program!")
                break
        except:
            print("ERROR!")
            print("Some issue has occured, please try again!")






        
