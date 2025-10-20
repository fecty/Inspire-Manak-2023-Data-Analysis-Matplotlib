import pandas as pd
import matplotlib.pyplot as plt
def per_district_participants_bar(series: pd.Series, threshold=300):
    """
    Horizontal bar chart of participants per district.
    Districts below threshold are grouped into 'Other Districts'.
    """
    mask = series < threshold
    other_sum = series[mask].sum()
    series2 = series[~mask].sort_values(ascending=True)
    if other_sum > 0:
        series2['Other Districts'] = other_sum

    fig, ax = plt.subplots(figsize=(12, max(8, len(series2)//5)))
    bars = series2.plot.barh(ax=ax, color='green')

    for bar in bars.patches:
        width = bar.get_width()
        ax.text(width + max(series2)*0.01,
                bar.get_y() + bar.get_height()/2,
                str(width), va='center', fontsize=9)

    ax.set_xlabel("Number of Participants")
    ax.set_ylabel("District")
    ax.set_title("Participants per District (Small districts grouped as 'Other')",
                 fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()