import pandas as pd
import matplotlib.pyplot as plt
def students_per_grade_bar(df: pd.DataFrame):
    grade_counts = df['Class'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = grade_counts.plot.barh(ax=ax, color='cornflowerblue')

    for bar in bars.patches:
        width = bar.get_width()
        ax.text(width + max(grade_counts)*0.01,
                bar.get_y() + bar.get_height()/2,
                str(width), va='center', fontsize=10)

    ax.set_xlabel("Number of Participants")
    ax.set_ylabel("Grade/Class")
    ax.set_title("Number of Students per Grade/Class", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()