
import pandas as pd

def check_data_quality(df):
    missing = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())
    invalid_quantity = int((df["quantity"] <= 0).sum())
    invalid_price = int((df["price"] <= 0).sum())

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
            missing,
            duplicates,
            invalid_quantity,
            invalid_price
        ],
        "Status": [
            "INFO",
            "PASS" if missing == 0 else "FAIL",
            "PASS" if duplicates == 0 else "FAIL",
            "PASS" if invalid_quantity == 0 else "FAIL",
            "PASS" if invalid_price == 0 else "FAIL"
        ]
    })

    return report
