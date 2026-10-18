
# Open Source Data Quality Analyzer

## Project Overview
A Python-based tool that analyzes CSV files and identifies common data quality issues.

## Features
- Detects missing values
- Identifies duplicate rows
- Detects invalid quantities and prices
- Validates required columns
- Generates a data quality report in CSV format
- Handles missing files and errors

## Technologies Used
- Python
- Pandas
- Jupyter Notebook


## Project Files

- `main_analyzer.py` — Main Python analyzer script
- `sample_sales.csv` — Sample sales dataset
- `sample_sales_2.csv` — Second sample dataset
- `day31_quality_report.csv` — Generated data quality report
- `day31_main_analyzer.ipynb` — Jupyter notebook for testing

## Future Improvements

- Add more data validation rules
- Create interactive visualizations
- Support more CSV datasets


## How to Run
```bash
python main_analyzer.py sample_sales_2.csv
```

## Output
The analyzer displays a data quality report and saves it as `day31_quality_report.csv`.

## Author
Anu Jangid
