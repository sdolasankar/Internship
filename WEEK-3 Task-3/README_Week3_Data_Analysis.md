# Week 3 – Introduction to Data Analysis (Pandas)

This folder contains the files for **Week 3: Introduction to Data Analysis – Working with Real Data**.

## Files

- `week3_data_analysis.ipynb` – Jupyter Notebook with all the code and explanations.
  - Creates a simple sales dataset
  - Saves it to `sales_data.csv`
  - Reads the CSV using pandas
  - Explores the data (head, shape, info, describe)
  - Checks and handles missing values
  - Calculates basic statistics (mean, max, min)
  - Performs a mini **Sales Analysis Project**:
    - Adds a `Total` (Quantity × Price) column
    - Calculates total sales
    - Finds the best-selling product
    - Shows a simple sales summary report

## Requirements

- Python 3.x
- `pandas` library
- Jupyter Notebook / JupyterLab / VS Code / Google Colab

To install pandas, run:

```bash
pip install pandas
```

## How to Run the Notebook

1. Open Jupyter Notebook or JupyterLab.
2. Copy `week3_data_analysis.ipynb` into your working folder.
3. Start Jupyter and open the notebook.
4. Run the cells from top to bottom.

If you are using **Google Colab**:

1. Upload `week3_data_analysis.ipynb` to Colab.
2. Run each cell in order.

## Using Your Own Dataset

If you want to use your own CSV file instead of the example sales data:

1. Place your CSV file in the same folder as the notebook.
2. Change the `csv_filename` variable in the notebook to your file name, e.g.:

```python
csv_filename = "my_marks.csv"
```

3. Make sure the column names in your dataset match the columns you use in the code.

## What This Task Shows

This task demonstrates that you understand:

- What data analysis is and why it is important
- How to use pandas for Excel-like operations in Python
- How to load, explore, clean, and analyze real data
- How to build a very simple end-to-end data analysis project

You can submit this notebook and README file as your **Week 3 Data Analysis task**.
