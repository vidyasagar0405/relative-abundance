#!/usr/bin/env python3

import sys
import pandas as pd

def add_column(df: pd.DataFrame, column_name: str, string: str) -> pd.DataFrame:
    df[column_name] = string
    return df

def main():
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]

    df = pd.read_csv(input_csv)
    new_df = add_column(df, "experiment_type", "amplicon")
    new_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    main()
