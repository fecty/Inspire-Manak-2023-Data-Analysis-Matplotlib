import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from analysis_functions import *



def main(csv_file: str):
    df = pd.read_csv(csv_file)
    s1 = df['State Name'].value_counts()
    s2 = df['District Name'].value_counts()

    menu = {
        "1": ("Participants per State (Pie Chart)", lambda: per_state_participants_piechart(s1)),
        "2": ("Participants per District (Bar Chart)", lambda: per_district_participants_bar(s2)),
        "3": ("Gender-wise Participation (Pie Chart)", lambda: gender_participation_pie(df)),
        "4": ("Scholarship Amount per Category (Bar Chart)", lambda: scholarship_by_category_bar(df)),
        "5": ("Students per Grade/Class (Bar Chart)", lambda: students_per_grade_bar(df)),
        "0": ("Exit", None)
    }

    while True:
        print("\nSelect a plot to display:")
        for key, (desc, _) in menu.items():
            print(f"{key}: {desc}")

        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("Exiting...")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main("../assets/INSPIRE_MANAK.csv")
