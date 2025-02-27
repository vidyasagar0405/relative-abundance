import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = "./src/relative_abundance/exercise1-lite.csv"

def plot_top_quantile(df:pd.DataFrame ,quantile:float, aspect:float):
    # Select the top 20 rows based on descending order of 'sample-count'
    df= df.sort_values(by='sample-count', ascending=False)

    top_quartile = df["sample-count"].quantile(quantile)
    df_top = df[df['sample-count'] > top_quartile]

    sns.set_theme(style="white")

    g = sns.catplot(
        data=df_top,
        kind="bar",
        x="id",
        y="sample-count",
        # palette="dark",
        # alpha=0.6,
        height=6,
        aspect=aspect,
        hue="id",
        legend=False,
    )
    g.set_axis_labels("study-id", "samples count")

    # Rotate x-axis labels by 90 degrees
    plt.setp(g.ax.get_xticklabels(), rotation=90)
    g.savefig(f"sample_count_bar_top_quantile_{quantile}.svg")


def main():
    df = pd.read_csv(file)
    plot_top_quantile(df, 0.85, 2)
    plot_top_quantile(df, 0.90, 2)
    plot_top_quantile(df, 0.95, 2)

if __name__ == "__main__":
    main()
