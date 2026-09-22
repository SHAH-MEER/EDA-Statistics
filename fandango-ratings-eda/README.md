# Fandango Ratings Bias Case Study

A Python and Quarto case study asking whether Fandango's 2015 movie ratings were
systematically inflated above the rating actually implied by user votes, and above
what other major review platforms scored the same films. Based on the data behind
FiveThirtyEight's 2015 investigation *Be Suspicious of Online Movie Ratings,
Especially Fandango's*. The write-up moves from Fandango's own displayed stars
versus its true underlying rating, through pairwise critic-versus-user comparisons
on Rotten Tomatoes and Metacritic, to a normalized comparison across all platforms,
closing with a check of whether the inflation is concentrated in obscure titles or
runs largest on Fandango's most-voted films.

## Data

Source: FiveThirtyEight's public GitHub repository
[fivethirtyeight/data](https://github.com/fivethirtyeight/data/tree/master/fandango),
pulled by FiveThirtyEight on 2015-08-24. Two files are used:

- `data/fandango_scrape.csv`: every film Fandango displayed a rating for, with the
  displayed star rating, the underlying numeric rating pulled from each page's HTML,
  and the vote count (504 films).
- `data/all_sites_scores.csv`: the subset of those films (146) that also had a
  Rotten Tomatoes critic and user score, a Metacritic critic and user score, and an
  IMDb score, plus at least 30 Fandango fan reviews.

Both files are included in this repository, so no download is needed to reproduce
this analysis.

## Reproducing

Requires Python 3.11 or later and Quarto. Install the packages used in the analysis:

```bash
pip install pandas numpy scipy matplotlib seaborn
```

Then render the document from inside this folder:

```bash
quarto render fandango-ratings-eda.qmd
```

This produces `fandango-ratings-eda.html`, a self-contained report with no external
dependencies. The rendered HTML is not tracked in this repository; render it locally
to view it.

## Structure

- `fandango-ratings-eda.qmd`: the report source
- `data/fandango_scrape.csv`: Fandango's displayed stars vs. true rating, all 504 films
- `data/all_sites_scores.csv`: Rotten Tomatoes, Metacritic, and IMDb scores for the
  146 films with sufficient review coverage
- `images/taken3-poster.jpg`: local copy of the *Taken 3* poster used in the report,
  downloaded from Wikimedia; kept locally because Quarto's `embed-resources` fetch
  is rejected by Wikimedia's User-Agent policy at render time
- `references.bib`: citations for the data source
- `styles.css`: layout tweaks (content width, padding) applied on top of Quarto's
  default HTML theme
- `Fandango_case_study.ipynb`: the original exploratory notebook this report was
  ported from
