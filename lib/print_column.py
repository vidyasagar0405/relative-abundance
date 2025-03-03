import pandas as pd
import sys


def print_column(df: pd.DataFrame, column: str):

    entries = [ i for i in df[column] ]

    for entry in entries:
        print(entry)


def main():
    input = sys.argv[1]
    column = sys.argv[2]

    df = pd.read_csv(input)

    print_column(df, column)


if __name__ == "__main__":
    main()
