import yfinance as yf
import pandas as pd

class Call:
    def __init__(self, ticker, strike, expiry):
        self.ticker = ticker
        self.yf_ticker = yf.Ticker(ticker)
        self.df = pd.DataFrame()

    def payoff(self, strike, expiry):
        # Implement the payoff calculation for call options
        pass

class Put:
    def __init__(self, ticker):
        self.ticker = ticker
        self.yf_ticker = yf.Ticker(ticker)
        self.df = pd.DataFrame()

def get_yf_options(ticker):
    """
    Collects all calls and puts with openInterest for a given ticker.
    """

    yf_ticker = yf.Ticker(ticker)
    options = yf_ticker.options
    calls = []
    puts = []

    for expiry in options:
        opt_chain = yf_ticker.option_chain(expiry)
        calls.extend(opt_chain.calls[opt_chain.calls['openInterest'] > 0].to_dict('records'))
        puts.extend(opt_chain.puts[opt_chain.puts['openInterest'] > 0].to_dict('records'))

    return calls, puts
