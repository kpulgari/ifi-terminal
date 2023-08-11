from utils.table_renders import render_default_terminal, render_reddit_terminal, render_finnhub_terminal, render_yfinance_terminal

from rich.console import Console


if __name__ == "__main__":
    while True:
        try:
            selection = input(
                "Select: \n [D] for default ifi_terminal display \n [Y] for <yfinance> (traditional financial information) \n [R] for <reddit> data \n [F] for <finnhub> (trend analysis bots) \nPress any other key to exit application: ").upper()
    
            if selection == "D":
                render_default_terminal()
    
            elif selection == "Y":
                render_yfinance_terminal()
    
            elif selection == "R":
                render_reddit_terminal()
    
            elif selection == "F":
                print(
                    "Welcome to ifi_terminal's decision helper! We currently offer 4 trend analyses:")
                print("1. Bot 1: Display percent change for select stocks")
                print("2. Bot 2: Bull/Bear indicator chart")
                print(
                    "3. Bot 3: Trading gap identification - fundamental for sentiment analysis")
                print(
                    "4. Bot 4: Optimistic Trend Check: Is low of the day is higher than the closing price of the previous day?")
                choice = input(
                    "Please enter the number of the bot you would like to view: ")
    
                console = Console()
                table = render_finnhub_terminal(choice, False)
                console.print(table)
    
            else:
                print("Exiting Program!")
                break
        except:
            print("ERROR!")
            print("Some issue has occured, please try again!")
