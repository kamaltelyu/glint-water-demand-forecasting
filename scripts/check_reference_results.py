#!/usr/bin/env python3
import argparse
from pathlib import Path
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
        description="Check the final GLINT manuscript-readiness gate."
    )
    parser.add_argument(
        "csv",
        nargs="?",
        default="results/reference_readiness_gate.csv",
        help="Path to MANUSCRIPT_READINESS_GATE.csv",
    )
    args = parser.parse_args()

    path = Path(args.csv)
    df = pd.read_csv(path)

    expected = {("BWDF", 24), ("BWDF", 72), ("BWDF", 168), ("BWDF", 336),
                ("SOWEKI", 24), ("SOWEKI", 72), ("SOWEKI", 168), ("SOWEKI", 336)}
    observed = set(zip(df["dataset"], df["horizon"]))

    print(f"File: {path}")
    print(f"Rows: {len(df)}")
    print(f"All 8 dataset-horizon settings present: {observed == expected}")
    print(f"GLINT MASE < 1 in: {(df['GLINT_MASE'] < 1).sum()}/8")
    print(f"GLINT best main model in: {df['GLINT_is_best'].astype(bool).sum()}/8")
    print()
    print(df[
        ["dataset", "horizon", "GLINT_MASE",
         "best_baseline", "best_baseline_MASE",
         "improvement_vs_best_baseline_pct"]
    ].to_string(index=False))

if __name__ == "__main__":
    main()
