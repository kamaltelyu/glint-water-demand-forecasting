# GLINT Water-Demand Forecasting

Reproducibility code for the manuscript:

**GLINT: Multi-Seasonal Residual Gating in a Linear–Transformer for Cross-Dataset Multi-Horizon Water Demand Forecasting**

GLINT combines explicit daily and weekly seasonal forecasts, residual linear and multi-scale Transformer experts, and step-wise adaptive gating conditioned by residual statistics, latent Transformer context, and known-future calendar features.

## Experimental protocol

- **Datasets:** BWDF (10 DMA series) and SOWEKI (11 operational demand series)
- **Resolution:** hourly
- **Lookback:** 336 h
- **Forecast horizons:** 24, 72, 168, and 336 h
- **Split:** chronological 70% / 15% / 15%
- **Seeds:** 42, 123, 456
- **Main baselines:** Seasonal Naive 168, Direct Linear, DLinear, LSTM, Patch Transformer
- **Ablations:** No Transformer, No Linear, Static Gate, No Calendar, Raw Transformer
- **Statistics:** series-level paired two-sided Wilcoxon signed-rank tests with Holm correction and rank-biserial effect sizes
- **Efficiency:** parameter count, training time, inference latency, throughput, and peak GPU memory

## Repository structure

```text
.
├── notebooks/
│   └── GLINT_Final_Reproducibility.ipynb
├── results/
│   ├── README.md
│   └── reference_readiness_gate.csv
├── figures/
│   ├── Figure1_GLINT_Conceptual_Architecture.drawio
│   └── Figure1_GLINT_fixed.png
├── docs/
│   └── REPRODUCIBILITY.md
├── scripts/
│   └── check_reference_results.py
├── CITATION.cff
├── requirements.txt
└── README.md
```

## Data

The repository does **not** redistribute raw datasets. The notebook loads/downloads data programmatically.

### BWDF
BWDF DMA inflows are loaded through the `wf4bwdf` Python package.

### SOWEKI
Zenodo record **19627517**, DOI **10.5281/zenodo.19627517**. Source observations are aggregated to hourly means so the target remains a rate in m3/h.

Please consult the original data sources for their licenses and terms of use.

## Running the experiment

The recommended environment is **Google Colab with a GPU runtime**.

1. Open `notebooks/GLINT_Final_Reproducibility.ipynb`.
2. Select a GPU runtime.
3. Run all cells from top to bottom.
4. Allow Google Drive mounting when prompted.
5. The notebook writes experiment artifacts under `/content/drive/MyDrive/MFL_WaterDemand_FINAL_IJIES/`.

The implementation uses causal missing-input reconstruction, train-only robust scaling, masked target evaluation, validation-only configuration selection, and series-level statistical testing. See `docs/REPRODUCIBILITY.md` for details.

## Reference results

The final experiment achieved the lowest MASE among the main compared models in all eight dataset-horizon settings. The exact reference values are stored in `results/reference_readiness_gate.csv`.

Ablation results are interpreted separately: the Transformer expert provides dataset-dependent value, while seasonal residualization, the linear residual path, and adaptive gating provide the most consistent contributions.

## Implementation naming note

This repository has been updated from the earlier working name **GLINT** to the final manuscript name **GLINT**. The experiment logic and reported numerical results are unchanged; the update is a naming and documentation alignment with the manuscript.

## Citation

Citation metadata are provided in `CITATION.cff`. Update the DOI and final journal bibliographic information after publication.

## License

No software license is assigned yet. Add the authors' preferred license before a public software release if required.
