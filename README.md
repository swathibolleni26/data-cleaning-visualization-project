# Data Cleaning & Visualization Project

## About the Project

This project focuses on cleaning and analyzing a student dataset using Python. The dataset contains missing values, outliers, and duplicate records, which are common problems in real-world data.

The main goal of this project is to learn how to prepare raw data for analysis and create visualizations that help understand the data better.

---

## What I Did

In this project, I:

* Created a student dataset
* Identified and handled missing values
* Detected and treated outliers using the IQR method
* Removed duplicate records
* Generated different visualizations using Matplotlib and Seaborn
* Created a report containing important insights from the data

---

## Tools and Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Project Structure

```text
Data_Project/
│
├── data_cleaning_visualization.py
├── README.md
│
└── output/
    ├── raw_dataset.csv
    ├── cleaned_dataset.csv
    ├── dashboard_report.txt
    │
    └── visualizations/
        ├── cgpa_distribution.png
        ├── programming_languages.png
        ├── cgpa_vs_projects.png
        ├── internship_vs_cgpa.png
        ├── age_distribution.png
        └── grade_by_language.png
```

---

## Key Features

### Missing Value Handling

Missing values in the dataset were replaced using:

* Median for numerical columns
* Mode for categorical columns

### Outlier Detection

Outliers were identified using the Interquartile Range (IQR) method and treated appropriately.

### Duplicate Removal

Duplicate records were detected and removed to improve data quality.

### Data Visualization

Several charts were created to understand patterns and relationships in the dataset.

The visualizations include:

* CGPA Distribution
* Programming Language Distribution
* CGPA vs Projects Completed
* Internship Hours vs CGPA
* Age Distribution
* Grade Distribution Heatmap

---

## Results

After cleaning the dataset:

* Total students analyzed: 200
* Average CGPA: 7.58
* Median Age: 20 years
* Average Projects Completed: 4.6
* Average Internship Hours: 49.4
* Most Popular Programming Language: Python

---

## What I Learned

Through this project, I learned:

* Data cleaning techniques
* Handling missing values
* Detecting and treating outliers
* Removing duplicate records
* Creating visualizations using Python
* Understanding and presenting insights from data

---

## How to Run the Project

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

Run the Python file:

```bash
python data_cleaning_visualization.py
```

---

## Conclusion

This project helped me understand the complete process of data preprocessing and visualization. It provided hands-on experience in working with raw data, improving data quality, and presenting meaningful insights through charts and reports.
