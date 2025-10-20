import pandas as pd
import matplotlib.pyplot as plt

def per_state_participants_piechart(series: pd.Series, threshold=1000):
    """
    Pie chart of participants per state.
    States below threshold are grouped into 'Other States'.
    """
    # Group small values into 'Other'
    mask = series < threshold
    if mask.any():
        other_sum = series[mask].sum()
        series = series[~mask]
        series.loc['Other States'] = other_sum

    series = series.sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts, autotexts = ax.pie(
        series,
        labels=series.index,
        autopct="%1.1f%%",
        pctdistance=.8,
        labeldistance=1.1,
        startangle=0,
        radius=1.1,
    )

    ax.legend(
        wedges, series.index,
        title="States",
        loc="upper right",
        bbox_to_anchor=(1, 0, 0.13, 1)
    )
    ax.axis('equal')
    ax.set_title("Total Number of Grants Approved Per State")
    plt.show()