# INSPIRE MANAK Data Analysis Tool

This tool provides a set of visualizations for analyzing data from the INSPIRE MANAK project.

## Features

- **Participants per State (Pie Chart):** Visualizes the distribution of participants across different states.
- **Participants per District (Bar Chart):** Shows the number of participants from each district.
- **Gender-wise Participation (Pie Chart):** Displays the proportion of male and female participants.
- **Scholarship Amount per Category (Bar Chart):** Compares the scholarship amounts awarded to different categories.
- **Students per Grade/Class (Bar Chart):** Illustrates the number of students in each grade or class.

## Getting Started

1.  **Prerequisites:**

    - Python 3.x
    - Libraries: pandas, numpy, matplotlib

    ```bash
    pip install pandas numpy matplotlib
    ```

2.  **Running the Tool:**

    ```bash
    python src/main.py
    ```

    The script reads data from `assets/INSPIRE_MANAK.csv`. Ensure this file exists in the `assets` directory relative to the script's location.

## Project Structure

```
.
├── assets
│   └── INSPIRE_MANAK.csv       # CSV data file
├── src
│   └── main.py                 # Main script with analysis and menu
├── analysis_functions.py       # Helper functions for generating plots
└── README.md                   # This file
```

## Usage

After running the script, a menu will appear in the console. Enter the number corresponding to the desired plot to display it. Enter `0` to exit.

## Notes

- The quality of the visualizations depends on the data in `INSPIRE_MANAK.csv`.
- Ensure that the required libraries are installed before running the script.
