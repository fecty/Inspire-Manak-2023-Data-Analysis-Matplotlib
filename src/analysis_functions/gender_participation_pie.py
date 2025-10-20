import pandas as pd
import matplotlib.pyplot as plt

def gender_participation_pie(df: pd.DataFrame):
    gender_counts = df['Gender'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(gender_counts,
           labels=gender_counts.index,
           autopct='%1.1f%%',
           startangle=90,
           colors=['skyblue', 'pink'])
    ax.set_title("Participants by Gender", fontsize=16, fontweight='bold')
    ax.axis('equal')
    plt.show()