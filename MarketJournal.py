"""
@Today's Date : 10/5/2022

@Author : Thomas Barker
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date


def stock_prices(data):
    today = date.today()
    day = today.strftime("%B %d, %Y")
    daily_stocks = [day]
    for link in data:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        price_tag = soup.find('span', class_="QuoteStrip-lastPrice")
        price = price_tag.text
        if link == "https://www.cnbc.com/quotes/JP10Y?qsearchterm=Japan%2010" \
                   "%20year" or link == \
                "https://www.cnbc.com/quotes/DE10Y?qsearchterm=bund%2010" or \
                link == "https://www.cnbc.com/quotes/UK10Y?qsearchterm=uk10" \
                or link == "https://www.cnbc.com/quotes/US10Y?qsearchterm=US10":
            last = len(price)
            price = price[:last - 1]
        daily_stocks.append(price)
    print(daily_stocks)
    return daily_stocks

data = ["https://www.cnbc.com/quotes/EUR=",
            "https://www.cnbc.com/quotes/GBP=",
            "https://www.cnbc.com/quotes/JPY=",
            "https://www.cnbc.com/quotes/CNY=",
            "https://www.cnbc.com/quotes/.N225",
            "https://www.cnbc.com/quotes/.GDAXI?qsearchterm=DAX",
            "https://www.cnbc.com/quotes/.FTSE?qsearchterm=FTSE",
            "https://www.cnbc.com/quotes/.DJI?qsearchterm=DJIA",
            "https://www.cnbc.com/quotes/.SPX?qsearchterm=S%26P",
            "https://www.cnbc.com/quotes/JP10Y?qsearchterm=Japan%2010%20year",
            "https://www.cnbc.com/quotes/DE10Y?qsearchterm=bund%2010",
            "https://www.cnbc.com/quotes/UK10Y?qsearchterm=uk10",
            "https://www.cnbc.com/quotes/US10Y?qsearchterm=US10",
            "https://www.cnbc.com/quotes/%40GC.1?qsearchterm=Gold",
            "https://www.cnbc.com/quotes/%40LCO.1?qsearchterm=brent",
            "https://www.cnbc.com/quotes/BTC.CB%3D?qsearchterm=bitcoin", ]

df = pd.read_csv(r'C:\Users\tbark\OneDrive - Duke University\BarkerAutomatedMarketJournal.csv')
df.loc[len(df.index)] = stock_prices(data)
print(df)
df.to_csv(r'C:\Users\tbark\OneDrive - Duke University\BarkerAutomatedMarketJournal.csv', index=False)

# if __name__ == '__main__':
    # column_names = ["DATE", "EURO/USD",	"STG/USD", "USD/YEN", "USD/CNY",
    #                 "NIKKEI", "DAX", "FTSE", "DOW",	"S&P", "JAPAN 10 YR (%)",
    #                 "GERMAN 10 YR (%)",	"UK 10 YR (%)", "US 10 YR (%)",
    #                 "GOLD", "BRENT CRUDE", "BITCOIN"]
    # data = ["https://www.cnbc.com/quotes/EUR=",
    #         "https://www.cnbc.com/quotes/GBP=",
    #         "https://www.cnbc.com/quotes/JPY=",
    #         "https://www.cnbc.com/quotes/CNY=",
    #         "https://www.cnbc.com/quotes/.N225",
    #         "https://www.cnbc.com/quotes/.GDAXI?qsearchterm=DAX",
    #         "https://www.cnbc.com/quotes/.FTSE?qsearchterm=FTSE",
    #         "https://www.cnbc.com/quotes/.DJI?qsearchterm=DJIA",
    #         "https://www.cnbc.com/quotes/.SPX?qsearchterm=S%26P",
    #         "https://www.cnbc.com/quotes/JP10Y?qsearchterm=Japan%2010%20year",
    #         "https://www.cnbc.com/quotes/DE10Y?qsearchterm=bund%2010",
    #         "https://www.cnbc.com/quotes/UK10Y?qsearchterm=uk10",
    #         "https://www.cnbc.com/quotes/US10Y?qsearchterm=US10",
    #         "https://www.cnbc.com/quotes/%40GC.1?qsearchterm=Gold",
    #         "https://www.cnbc.com/quotes/%40LCO.1?qsearchterm=brent",
    #         "https://www.cnbc.com/quotes/BTC.CB%3D?qsearchterm=bitcoin", ]
    # df = pd.DataFrame(columns = column_names)
    # print(df)
    # df.loc[len(df.index)] = stock_prices(data)
    # print(df)
    # df.to_csv(r'C:\Users\tbark\OneDrive - Duke '
    #           r'University\BarkerAutomatedMarketJournal.csv', index=False)

    # df = pd.read_csv(r'C:\Users\tbark\OneDrive - Duke University\BarkerAutomatedMarketJournal.csv')
    # df.loc[len(df.index)] = stock_prices(data)
    # print(df)
    # df.to_csv(r'C:\Users\tbark\OneDrive - Duke '
    #           r'University\BarkerAutomatedMarketJournal.csv', index=False)

    #export dataframe to excel
    # df.to_excel(r'C:\Users\tbark\OneDrive - Duke University\Barker Market '
    #             r'Journal Fall 2022.xlsx', sheet_name = 'Test1', index= False)