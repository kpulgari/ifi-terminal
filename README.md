## Project Introduction

Our project, IFI (Instant Financial Information) Terminal, is a easy-to-use software application that simplifies and streamlines the process of accessing real-time financial information. IFI Terminal includes both static and personalized tables using Python's rich library to display information on stocks from both `yFinance` and `Finnhub` APIs, as well as a module that utilizes `Reddit` API to fetch popular posts from financial subreddits like `r/wallstreetbets`.

While a similar application - Bloomberg Terminal - provides similar features and tools for financial professionals, our application is much more lightweight and user-friendly, making it ideal for new investors or those who want a simpler way to view financial information. Additionally, IFI Terminal can be run directly in the user's terminal without requiring separate software installation or subscription.

## Demo
[![IFI Terminal](https://user-images.githubusercontent.com/90290549/236655150-322af4b7-b1e3-4fb0-afdf-95629e3d1302.png)](https://drive.google.com/file/d/1jaHfjvsNJg4x4zcLPFz05_uAKi_7Y6Ny/view)

## Technical Architecture

To provide a comprehensive understanding of the architecture of our application, we created a diagram of our program's components and their interactions:

### Architecture Diagram

<img width="889" alt="Screenshot 2023-05-03 at 4 56 17 PM" src="https://user-images.githubusercontent.com/90290549/236059501-a16a5165-55a7-4775-82e8-fc78b1f08a9b.png">

### Backend:

Our backend consists of three modules that interact with different APIs: `yFinance`, `Finnhub`, and `Reddit`. Each module is stored in our `utils` folder and has specific functions to fetch and process data from their respective APIs. The `main.py` app imports these modules and calls their functions as needed to retrieve data for display on the frontend tables.

- `yFinance` Interactor: Provides fundamental information related to classical trading principles. It has live updates and provides near-instantaneous information for investors to make trades.
- `Finnhub` Interactor: Used for newer, more experimental trading methods. We provide analytical bots that draw insights from the market and present them in an easy-to-understand visual manner.
- `Reddit` Interactor: Fetches popular posts and comments from specified subreddits, and can be expanded to draw insights from these.

Finally, we have a bash script `ifi_terminal.sh` that executes the code as needed.

### Frontend:

Our frontend uses the `rich` library from Python to generate elegant and personalized tables that display real-time information. The frontend requests data from the backend by calling their respective functions and receives the response to display on the tables. The tables can be customized through user input in the terminal.

- `main.py`: All group members worked on the frontend module of the `main.py` app, which uses the `rich` library to generate tables and the `Live` module to update them in real-time.

## Installation  and Running Instructions

1. Clone the repository from GitHub
2. Navigate to root directory and run following commands to set up Conda virtual environment and install dependencies:
   ```
   conda env create -f environment.yml
   conda activate ifi_terminal
   ```
3. **Security Step:** *There is a file named `secret_template.py` in the utils directory. Please fill in the necessary information and rename the file to `secrets.py`. This will allow developers to make changes to the application without revealing access tokens (since it's part of the `.gitignore` file), and users won't need to perform any additional authentication.*
4. To start the program:
   1. Run `bash ifi_terminal.sh`
   2. If that does not work and you get some error try the following commands:
      ```
      cd src
      py main.py

      # or try
      python main.py
      ```
5. Follow the directions in the terminal to interact with the program!

## Future Developments:

Our application offers a significant advantage by providing access to nearly all types of financial market data. As we continue to enhance the app, we can expand its capabilities to encompass additional tools like predictive models, technical analysis, and other features that traders may find useful in making decisions. Although our current GUI is terminal-based and displays text-only information, we plan to incorporate charts, guiding features, and predictive models in future iterations while keeping it lightweight and easy to use on the terminal.

## Group Roles

**Siddarth Aananth**: Responsible for `Finnhub` API interactor and `main.py` frontend

**Suchit Bapatla**: Responsible for `Reddit` API interactor and `main.py` frontend

**Sambuddha Biswas**: Responsible for `Reddit` API interactor and `main.py` frontend

**Kaushik Pulgari**: Responsible for `yFinance` API interactor and `main.py` frontend
