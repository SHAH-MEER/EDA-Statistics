# Financial Markets Return Normality Case Study

A Python and Quarto case study asking whether daily financial market returns are
normally distributed, and what breaks in models, like Value-at-Risk, that assume
they are. The write-up moves from a visual first look at the return distributions,
through formal normality tests, volatility clustering, and autocorrelation, to a
rolling out-of-sample VaR backtest quantifying what a normal-distribution assumption
actually costs a risk model.

## Data

Source: Yahoo Finance via the `yfinance` package, adjusted daily close prices for
8 tickers chosen for sector spread: `SPY` (S&P 500 index), `AAPL` and `MSFT`
(technology), `JPM` (financials), `XOM` (energy), `JNJ` (healthcare), `KO` (consumer
staples), and `TSLA` (high-volatility growth). The window runs from 2011-01-01
through the most recent trading day, roughly 15 years, covering both the 2020 COVID
crash and the 2022 rate-hiking cycle.

The data is already included at `data/prices.csv` (all 8 tickers, full window) and
`data/spy_ohlcv.csv` (SPY only, last 6 months, used for the candlestick chart), so
no download is needed to reproduce this analysis. To refresh with current data:

```bash
python scripts/fetch_data.py
```

## Reproducing

Requires Python 3.11 or later and Quarto. Install the packages used in the analysis:

```bash
pip install yfinance pandas numpy scipy statsmodels matplotlib seaborn mplfinance joypy arch
```

Then render the document from inside this folder:

```bash
quarto render financial-markets-eda.qmd
```

This produces `financial-markets-eda.html`, a self-contained report with no external
dependencies. The rendered HTML is not tracked in this repository; render it locally
to view it.

## Structure

- `financial-markets-eda.qmd`: the report source
- `scripts/fetch_data.py`: one-time data pull; writes the two CSVs below
- `data/prices.csv`: daily adjusted close for all 8 tickers, 2011 to present
- `data/spy_ohlcv.csv`: SPY OHLCV, last 6 months, for the candlestick chart
- `references.bib`: citations for the statistical tests and models used
- `styles.css`: layout tweaks (content width, padding) applied on top of Quarto's
  default HTML theme
