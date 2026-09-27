# GLINT reference headline results

| dataset   |   horizon |   GLINT_MASE | best_baseline    |   best_baseline_MASE | improvement_vs_best_baseline_pct   |
|:----------|----------:|-------------:|:-----------------|---------------------:|:-----------------------------------|
| BWDF      |        24 |       0.7023 | DLinear          |               0.7705 | 8.85%                              |
| BWDF      |        72 |       0.7357 | DLinear          |               0.8108 | 9.26%                              |
| BWDF      |       168 |       0.7704 | DLinear          |               0.8391 | 8.18%                              |
| BWDF      |       336 |       0.8313 | SeasonalNaive168 |               0.905  | 8.14%                              |
| SOWEKI    |        24 |       0.653  | DLinear          |               0.75   | 12.93%                             |
| SOWEKI    |        72 |       0.6988 | SeasonalNaive168 |               0.8007 | 12.73%                             |
| SOWEKI    |       168 |       0.7408 | SeasonalNaive168 |               0.7966 | 7.01%                              |
| SOWEKI    |       336 |       0.8107 | SeasonalNaive168 |               0.8726 | 7.09%                              |

These values reproduce the manuscript headline comparison.
