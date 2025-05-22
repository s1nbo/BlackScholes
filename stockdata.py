import yfinance as yf

def stockdata(ticker: str = 'AAPL', start: str ="2020-01-01", end: str = "2021-01-01"):
    """
    Fetches historical closing price data for a given stock ticker using Yahoo Finance.
    Parameters:
        ticker (str): The stock ticker symbol (default is 'AAPL').
        start (str): Start date for historical data in 'YYYY-MM-DD' format (default is '2020-01-01').
        end (str): End date for historical data in 'YYYY-MM-DD' format (default is '2021-01-01').
    Returns:
        pd.Series: A pandas Series containing the daily closing prices for the given ticker and date range.
    """
    
    return yf.download(ticker, start=start, end=end)['Close']
