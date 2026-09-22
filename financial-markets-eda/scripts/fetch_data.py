"""One-time data pull for the financial-markets-eda report.

Fetches ~15 years of daily adjusted close prices for all 8 tickers into
data/prices.csv, and 6 months of SPY OHLCV into data/spy_ohlcv.csv (used only
for the Section 2 candlestick chart). Run from the financial-markets-eda/
folder; the .qmd never calls yfinance itself, it only reads these two CSVs.
"""

from pathlib import Path

import pandas as pd
import yfinance as yf

TICKERS = ["SPY", "AAPL", "MSFT", "JPM", "XOM", "JNJ", "KO", "TSLA"]
START_DATE = "2011-01-01"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def fetch_prices():
    raw = yf.download(TICKERS, start=START_DATE, auto_adjust=True, progress=False)
    close = raw["Close"]
    long_form = (
        close.reset_index()
        .melt(id_vars="Date", var_name="ticker", value_name="adj_close")
        .rename(columns={"Date": "date"})
        .dropna(subset=["adj_close"])
        .sort_values(["ticker", "date"])
    )
    long_form["date"] = long_form["date"].dt.strftime("%Y-%m-%d")
    long_form.to_csv(DATA_DIR / "prices.csv", index=False)
    return long_form


def fetch_spy_ohlcv():
    raw = yf.download("SPY", period="6mo", auto_adjust=True, progress=False)
    raw.columns = raw.columns.get_level_values(0)
    ohlcv = raw.reset_index().rename(
        columns={
            "Date": "date",
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
        }
    )[["date", "open", "high", "low", "close", "volume"]]
    ohlcv["date"] = ohlcv["date"].dt.strftime("%Y-%m-%d")
    ohlcv.to_csv(DATA_DIR / "spy_ohlcv.csv", index=False)
    return ohlcv


if __name__ == "__main__":
    prices = fetch_prices()
    ohlcv = fetch_spy_ohlcv()
    print(f"prices.csv: {len(prices)} rows, tickers={sorted(prices['ticker'].unique())}")
    print(f"date range: {prices['date'].min()} to {prices['date'].max()}")
    print(f"spy_ohlcv.csv: {len(ohlcv)} rows, {ohlcv['date'].min()} to {ohlcv['date'].max()}")
