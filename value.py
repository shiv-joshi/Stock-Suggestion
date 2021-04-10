import yfinance as yf
import yahoofinancials as yfs
from yahoofinancials import YahooFinancials
import yahoo_finance as yahoo_finance

def valuation(ticker):
    yfs = YahooFinancials(ticker)
    tech = YahooFinancials('QQQ')
    stock = yf.Ticker(ticker)

    #get pe and eps
    print("Processing...")
    tech_pe = tech.get_pe_ratio()
    tech_eps = tech.get_earnings_per_share()

    print("Fetching Industry Data...")
    pe = yfs.get_pe_ratio()
    eps = yfs.get_earnings_per_share()

    yfs.get_current_percent_change()

    if pe=='None' or eps == 'None':
        print("Not enough data found! Try again.")
    else:
        #check ratios
        pe_check = (pe<=tech_pe)
        eps_check = (eps>=tech_eps)
        if pe_check==True and eps_check==True:
            print("Great investment! " + ticker + " is trading well compared to the tech sector in terms of P/E and EPS.")
        elif (pe_check==True and eps_check==False) or (pe_check==False and eps_check==True):
            print("Good investment! " + ticker + " is trading well compared to the tech sector in terms of P/E and EPS.")
        else:
            print("Bad investment! " + ticker + " is trading poorly compared to the tech sector in terms of P/E and EPS.")
            
    print()
    print("For more insight here are some expert recommendations: ")
    print(stock.recommendations[['Firm', 'To Grade']])

def stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        print("1.Balance Sheet 2.Cashflow Statement 3.Earnings Statement 4.Quit")
        inp = input()
        
        while(inp!='4'):
            if inp=='1':
                print(stock.get_balance_sheet())
            elif inp=='2':
                print(stock.get_cashflow())
            elif inp=='3':
                print(stock.get_earnings())
            print("1.Balance Sheet 2.Cashflow Statement 3.Earnings Statement 4.Quit")
            inp = input()
    except:
        print("Not a valid ticker symbol.")

def live_data(ticker):
    try: 
        stock = YahooFinancials(ticker)
        data = {"Current Price:":stock.get_current_price(),
                "Percent Change:":round(stock.get_current_percent_change()*100,2),
                "Current Volume:":stock.get_current_volume(),
                "Today Open:":stock.get_open_price(),
                "Previous Close:":stock.get_prev_close_price(),
                "Today High:":stock.get_daily_high(),
                "Today Low:":stock.get_daily_low()}

        for k,v in data.items():
            print(k,v)
    except:
        print("Not a valid ticker symbol.")

print("Welcome! This app helps you find the right investment in the techonology industry.")
print("To start off, enter a stock...")

ticker = input("Ticker: ")
print("1. Stock Valuation")
print("2. Stock Info")
print("3. Live Stock Data")
choice = input()
print("----------------------------------------------------------------------------------")

if choice == '1':
    valuation(ticker)
elif choice == '2':
    stock_info(ticker)
elif choice == '3':
    live_data(ticker)
else: 
    print("Please enter a valid choice.")