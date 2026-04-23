# GitHub Cleanup Checklist — Weather Time Series Forecasting Project

Use this checklist before publishing the project on GitHub.

## 1. What to upload

For a clean public repo, upload the **project files**, not the zip file itself.

Best option:
- upload the contents of `source/src/` to the repo root

That means keeping files such as:
- `README.md`
- `.gitignore`
- `requirements.txt`
- `main.py`
- `part1_exploratory_preprocessing.py`
- `part2_ar_baseline.py`
- `part3_vanilla_rnn.py`
- `part4_attention_rnn.py`
- `part5_transformer.py`

Do **not** upload:
- `source.zip`
- `desktop.ini`
- `__pycache__/`
- `.pyc` files

## 2. Dataset decision

The project currently contains:
- `data/cleaned_weather.csv`

For a cleaner portfolio repo, it is usually better to **not commit the dataset** and instead mention in the README that it should be downloaded separately and placed at:

```text
data/cleaned_weather.csv
```

Reasons:
- keeps the repo lighter
- avoids uploading external dataset files unnecessarily
- makes the repo look more professional

## 3. Generated results decision

The project currently contains many generated files under:
- `plots/`
- `reports/`

Recommended public version:
- do **not** upload all generated plots and report files by default
- keep the code reproducible instead
- optionally select **2–4 representative figures** and place them in a small folder like `assets/`

This makes the repo cleaner and easier for recruiters to scan.

## 4. PDF report decision

You also uploaded a separate project report PDF.

Important: the report includes academic/course information and author names on the opening pages.

So decide one of these:

### Option A — safer public portfolio version
Do **not** upload the raw PDF report.

Why:
- it exposes course/university context
- it exposes co-author and academic cover-page details
- the README already summarizes the project well enough

### Option B — upload a report only if you want that public
If you want a report in the repo:
- rename it to something cleaner like `project_report.pdf`
- preferably use a cleaned version without the academic cover page
- make sure you are comfortable with the personal and academic details it contains

## 5. Repo structure to use

Recommended public structure:

```text
weather-time-series-forecasting/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── part1_exploratory_preprocessing.py
├── part2_ar_baseline.py
├── part3_vanilla_rnn.py
├── part4_attention_rnn.py
├── part5_transformer.py
└── assets/                # optional selected images only
```

Optional local-only folders when you run the code:

```text
data/
plots/
reports/
```

## 6. Things already worth keeping

This project is a good GitHub candidate because it already has:
- multiple forecasting methods
- a clear experimental pipeline
- reusable `.py` modules instead of only notebooks
- quantitative comparisons across multiple horizons
- both statistical and deep learning baselines

## 7. README honesty check

Before publishing, make sure the README matches the repo **exactly**.

If the repo does not contain a folder or file, do not claim it does.

## 8. Collaboration honesty check

If the project was collaborative, consider adding one short line in the README such as:

> This repository presents a cleaned portfolio version of a collaborative time-series forecasting project.

You do not need to mention the university or course if you do not want to, but you should avoid making collaborative work look like solo work if it was not.

## 9. Suggested repository names

Good public repo names:
- `weather-time-series-forecasting`
- `time-series-weather-forecasting`
- `weather-forecasting-model-comparison`

Best choice:
- `weather-time-series-forecasting`

## 10. Final upload recommendation

Upload now:
- `README.md`
- `.gitignore`
- `requirements.txt`
- all five `.py` files

Optional later:
- selected images in `assets/`
- cleaned report PDF

Avoid uploading now:
- `source.zip`
- `desktop.ini`
- `__pycache__`
- all raw generated plots/reports unless you intentionally want them public
- the dataset file unless you really want it in the repository
