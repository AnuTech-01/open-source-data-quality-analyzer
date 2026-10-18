

import sys

import pandas as pd
import os

def run_data_quality_analyzer(file_name):
    try:
        df = pd.read_csv(file_name)

        required_columns = [
            "order_id", "product", "quantity", "price", "city"
        ]

        missing_columns = [
            col for col in required_columns
            if col not in df.columns
        ]

        if missing_columns:
            print("Missing columns:", missing_columns)
            return None

        quantity = pd.to_numeric(df["quantity"], errors="coerce")
        price = pd.to_numeric(df["price"], errors="coerce")

        report = pd.DataFrame({
            "Check": [
                "Total Records",
                "Missing Values",
                "Duplicate Rows",
                "Invalid Quantities",
                "Invalid Prices"
            ],
            "Result": [
                len(df),
                int(df.isnull().sum().sum()),
                int(df.duplicated().sum()),
                int((quantity.isna() | (quantity <= 0)).sum()),
                int((price.isna() | (price <= 0)).sum())
            ]
        })

        report["Status"] = report.apply(
            lambda row: (
                "INFO" if row["Check"] == "Total Records"
                else "PASS" if row["Result"] == 0
                else "FAIL"
            ),
            axis=1
        )

        return report

    except FileNotFoundError:
        print("Error: CSV file not found:", file_name)
    except pd.errors.ParserError:
        print("Error: Invalid CSV format.")
    except Exception as e:
        print("Unexpected error:", e)

    return None



if __name__ == "__main__":
    file_name = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "day26_cleaned_sales.csv"
    )

    print("Open Source Data Quality Analyzer")
    print("Input file:", file_name)

    report = run_data_quality_analyzer(file_name)

    if report is not None:
        print("\nData Quality Report:")
        print(report.to_string(index=False))

        report.to_csv("day31_quality_report.csv", index=False)
        print("\nReport saved: day31_quality_report.csv")

