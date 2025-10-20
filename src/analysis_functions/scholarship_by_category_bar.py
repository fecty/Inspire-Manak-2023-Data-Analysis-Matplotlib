import pandas as pd
import matplotlib.pyplot as plt
def scholarship_by_category_bar(df: pd.DataFrame):
    category_amount = df.groupby('Category name')['Amount of Scholarship'].sum().sort_values()
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = category_amount.plot.barh(ax=ax, color='mediumseagreen')

    for bar in bars.patches:
        width = bar.get_width()
        ax.text(width + max(category_amount)*0.01,
                bar.get_y() + bar.get_height()/2,
                str(width), va='center', fontsize=10)

    ax.set_xlabel("Total Scholarship Amount")
    ax.set_ylabel("Category")
    ax.set_title("Total Scholarship Amount per Category", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()