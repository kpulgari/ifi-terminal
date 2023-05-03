# IFI Terminal
## Project Introduction

Our project, IFI (Instant Financial Information) Terminal, is a easy-to-use software application that simplifies and streamlines the process of accessing real-time financial information. IFI Terminal includes both static and personalized tables using Python's rich library to display information on stocks from both `yFinance` and `Finnhub` APIs, as well as a module that utilizes `Reddit` API to fetch popular posts from financial subreddits like `r/wallstreetbets`.

While a similar application - Bloomberg Terminal - provides similar features and tools for financial professionals, our application is much more lightweight and user-friendly, making it ideal for new investors or those who want a simpler way to view financial information. Additionally, IFI Terminal can be run directly in the user's terminal without requiring separate software installation or subscription.

## Technical Architecture
To provide a comprehensive understanding of the architecture of our application, we created a diagram of our program's components and their interactions:
### Architecture Diagram

### Backend:

Our backend consists of three modules that interact with different APIs: `yFinance`, `Finnhub`, and `Reddit`. Each module is stored in our `utils` folder and has specific functions to fetch and process data from their respective APIs. The `main.py` app imports these modules and calls their functions as needed to retrieve data for display on the frontend tables.

- `yFinance` Interactor: Kaushik worked on the yFinance interactor module, which fetches stock data from the yFinance API.
- `Finnhub` Interactor: Siddarth worked on the Finnhub interactor module, which fetches stock data from the Finnhub API.
- `Reddit` Interactor: Suchit and Sambuddha worked on the Reddit interactor module, which fetches popular posts and comments from specified subreddits.
### Frontend:

Our frontend uses the `rich` library from Python to generate elegant and personalized tables that display real-time information. The frontend requests data from the backend by calling their respective functions and receives the response to display on the tables. The tables can be customized through user input in the terminal.

- `main.py`: All group members worked on the frontend module of the `main.py` app, which uses the `rich` library to generate tables and the `Live` module to update them in real-time.
## Installation Instructions
1. Clone the repository from GitHub
2. Navigate to root directory and run following commands to set up Conda virtual environment and install dependencies:
    ```
    conda env create -f environment.yml
    conda activate ifi_terminal
    ```
3. Navigate to the `src` folder and start the application by running `python main.py`
4. Follow the directions on screen to interact with the program!
## Group Roles
**Siddarth Aananth**: Responsible for `Finnhub` API interactor and `main.py` functionalities

**Suchit Bapatla**: Responsible for `Reddit` API interactor and `main.py` functionalities

**Sambuddha Biswas**: Responsible for `Reddit` API interactor and `main.py` functionalities

**Kaushik Pulgari**: Responsible for `yFinance` API interactor and `main.py` functionalities