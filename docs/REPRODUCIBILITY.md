# GLINT reproducibility checklist

## Environment

Recommended:
- Google Colab
- GPU runtime
- Python environment supplied by Colab
- Packages installed by the notebook and/or `requirements.txt`

## Fixed experimental settings

| Item | Value |
|---|---|
| Lookback | 336 h |
| Forecast horizons | 24, 72, 168, 336 h |
| Weekly lag | 168 h |
| Daily lag | 24 h |
| Train / validation / test | 70 / 15 / 15% |
| Training stride | 6 h |
| Validation stride | 24 h |
| Test stride | 24 h |
| Seeds | 42, 123, 456 |
| Batch size | 256 |
| Maximum epochs | 25 |
| Early-stopping patience | 5 |
| Optimizer | AdamW |
| Learning rate | 1e-3 |
| Weight decay | 1e-4 |

## Final GLINT configuration

- `d_model = 32`
- `nhead = 4`
- Transformer layers = 1
- dropout = 0.05
- context dimension = 96
- gate dimension = 48
- local residual Transformer branch:
  - input = last 72 residual hours
  - patch = 12 h
  - stride = 6 h
- long residual Transformer branch:
  - input = 168 residual hours
  - patch = 24 h
  - stride = 12 h

## Evaluation

Metrics:
- MAE
- RMSE
- sMAPE
- MASE

Aggregation order:
1. forecast origins within series;
2. series within dataset;
3. random seeds for trainable models.

Series-level inference is used for statistical comparisons.

## Statistical testing

For each dataset and horizon:
- paired two-sided Wilcoxon signed-rank test;
- Holm correction across baseline comparisons;
- rank-biserial effect size;
- win/tie/loss count;
- bootstrap 95% confidence interval.

## Output integrity

The final run should preserve:
- all 10 BWDF series;
- all 11 SOWEKI series;
- four horizons for each dataset;
- three neural seeds.

Use `scripts/check_reference_results.py` to inspect a generated readiness-gate CSV.
