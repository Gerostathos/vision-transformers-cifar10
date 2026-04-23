# Weather Time Series Forecasting

## Overview

This repository contains an end-to-end time series forecasting project for weather measurements. The pipeline starts with preprocessing and exploratory analysis of a multivariate weather dataset and then compares four forecasting approaches on temperature prediction across multiple horizons:

- Autoregressive Ridge baseline
- Vanilla RNN
- Attention-based RNN
- Transformer encoder

The project focuses on forecasting the temperature variable (`T`) at **1-hour**, **6-hour**, and **24-hour** horizons and compares the models using standard regression and forecasting metrics.

## Project Goals

The main goals of the project are:

- prepare and analyze a real-world weather time series dataset
- apply both classical and neural forecasting methods
- compare short-, medium-, and longer-horizon forecasting performance
- study where simpler linear baselines remain competitive and where deep learning models help

## Dataset

The project uses the **Weather Long-term Time Series Forecasting** dataset from Kaggle.

The dataset contains roughly one year of weather measurements from 2020 and includes variables related to:

- pressure
- temperature and derived temperature variables
- humidity and vapor pressure
- wind speed and wind direction
- rainfall
- solar radiation and PAR measurements

For the experiments in this repository, the main prediction target is the **temperature feature `T`**.

## Preprocessing and EDA

The preprocessing and exploratory workflow includes:

- parsing the `date` column and using it as the time index
- checking for missing values
- resampling for exploratory analysis and forecasting horizons
- daily aggregation for trend and seasonal inspection
- STL decomposition of temperature
- correlation analysis on hourly weather variables
- wind direction circular encoding with `wd_sin` and `wd_cos`
- clipping non-physical negative values for variables such as rainfall
- log-transforming skewed variables such as `SWDR`
- time-based interpolation where needed
- ACF/PACF analysis for temperature diagnostics

## Models Implemented

### 1. Autoregressive Baseline

The statistical baseline is implemented as an **AR-style Ridge regression** model using lagged observations as predictors. This serves as a strong reference for short-term forecasting.

### 2. Vanilla RNN

A recurrent neural network is trained on rolling windows of past observations. The implementation includes:

- baseline training
- Optuna hyperparameter tuning
- a refined second tuning pass around the best trial

### 3. Attention RNN

The attention model is implemented as an **encoder-decoder GRU with Luong attention**, allowing the decoder to focus on the most relevant input time steps during prediction.

### 4. Transformer

The Transformer model uses:

- sinusoidal positional encoding
- multi-head self-attention
- supervised windows for sequence forecasting
- Optuna-based tuning and refinement

## Evaluation Metrics

The repository evaluates forecasts with:

- RMSE
- MAE
- MAPE / robust MAPE
- SMAPE
- WMAPE

## Main Results

A compact summary of the reported test-set results is shown below.

| Horizon | AR RMSE | AR MAE | AR MAPE | RNN RMSE | RNN MAE | RNN MAPE | ATTN RMSE | ATTN MAE | ATTN MAPE | TF RMSE | TF MAE | TF MAPE |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1-hour | 0.47 | 0.33 | 47.75 | 0.57 | 0.42 | 65.15 | 0.49 | 0.34 | 42.94 | 0.50 | 0.37 | 52.16 |
| 6-hour | 1.56 | 1.17 | 174.03 | 1.68 | 1.28 | 182.12 | 1.49 | 1.09 | 177.72 | 3.04 | 2.39 | 271.09 |
| 24-hour | 2.50 | 1.82 | 255.49 | 2.32 | 1.71 | 283.12 | 2.62 | 2.06 | 325.12 | 2.45 | 1.88 | 310.43 |

### High-level takeaways

- The **AR baseline** remains very competitive for very short-horizon forecasting.
- The **Attention RNN** performs strongest at the intermediate **6-hour** horizon.
- The **Vanilla RNN** achieves the best **RMSE/MAE** at the **24-hour** horizon among the reported neural results.
- The **Transformer** is competitive at 24 hours but unstable at 6 hours.
- Overall, no single model dominates all horizons.

## Repository Structure

A clean public version of the repository can be organized like this:

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
├── data/
│   └── cleaned_weather.csv          # local dataset, usually not committed
├── plots/                           # generated figures
└── reports/                         # generated PDFs and CSV summaries
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Place the dataset locally

Expected path:

```text
data/cleaned_weather.csv
```

### 3. Run the full pipeline

```bash
python main.py --csv data/cleaned_weather.csv --horizons 1 6 24
```

### Optional arguments

```bash
python main.py \
  --csv data/cleaned_weather.csv \
  --plot-dir ./plots \
  --report-dir ./reports \
  --horizons 1 6 24 \
  --train-ratio 0.70 \
  --val-ratio 0.20
```

## Outputs

Running the pipeline generates:

- per-part plot folders under `plots/`
- bundled PDF reports under `reports/`
- comparison CSV files for model evaluation

## Technologies Used

- Python
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- scikit-learn
- PyTorch
- Optuna

## Notes for a Public Portfolio Version

For a cleaner GitHub presentation, it is usually better to:

- keep the source code and README in the repository
- download the dataset separately instead of committing it
- optionally include only a few representative figures rather than every generated plot
- avoid committing caches, temporary files, and OS-specific files

## Future Improvements

Possible next improvements include:

- adding a small `assets/` folder with selected result figures shown in the README
- exporting the final comparison tables as cleaner markdown or image summaries
- separating reusable utility functions into helper modules
- adding reproducibility notes such as seeds, hardware details, and expected runtime
