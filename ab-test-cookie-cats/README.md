# Cookie Cats A/B Test Case Study

An R and Quarto case study on an A/B test run by the mobile game Cookie Cats, where a
progression gate was moved from level 30 to level 40 for a randomly assigned half of
players. The report is structured as a stakeholder-facing document: an executive
summary with the bottom-line recommendation, followed by numbered sections covering
whether the change worked, whether the experiment had enough statistical power, how
a frequentist and a Bayesian reading of the same data compare, the risk of stopping
the test early on repeated peeking, and a Day-7 confirmatory check, closing with a
collapsed appendix and a references list.

## Data

Source: [Mobile Games A/B Testing: Cookie Cats](https://www.kaggle.com/datasets/yufengsui/mobile-games-ab-testing)
on Kaggle, 90,189 players with columns for group assignment (`gate_30` / `gate_40`),
rounds played, and 1-day and 7-day retention.

The CSV is already included at `data/cookie_cats.csv`, so no download is needed to
reproduce this analysis.

## Reproducing

Requires R 4.5.1 or later and Quarto. The report's setup chunk installs nothing
automatically; install the required packages once:

```r
install.packages(c("tidyverse", "pwr", "gt", "scales", "broom"))
```

Then render the document from inside this folder:

```bash
quarto render ab-test-case-study.qmd
```

This produces `ab-test-case-study.html`, a self-contained report with no external
dependencies. The rendered HTML is not tracked in this repository; render it locally
to view it.

## Structure

- `ab-test-case-study.qmd`: the report source
- `data/cookie_cats.csv`: the dataset
- `references.bib`: citations used in the report
- `styles.css`: layout tweaks (content width, padding) applied on top of Quarto's
  default HTML theme
