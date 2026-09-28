import pandas as pd
from pathlib import Path


INPUT_FILE = Path("data/sales_raw.csv")
OUTPUT_FILE = Path("output/sales_clean.csv")


def load_data(file_path: Path) -> pd.DataFrame:
    """Load the raw CSV file."""
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize the sales dataset."""

    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    # 2. Remove duplicate rows
    df = df.drop_duplicates().copy()

    # 3. Clean text columns
    text_columns = df.select_dtypes(include=["object", "string"]).columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    # 4. Convert date column
    df["orderdate"] = pd.to_datetime(
        df["orderdate"],
        errors="coerce"
    )

    # 5. Convert numeric columns
    numeric_columns = [
        "unitprice",
        "quantity",
        "revenue",
        "deliverydays",
        "delayed",
        "customerid"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # 6. Remove rows with invalid essential values
    essential_columns = [
        "orderid",
        "orderdate",
        "revenue",
        "customerid"
    ]

    df = df.dropna(subset=essential_columns).copy()

    # 7. Validate delayed flag
    df["delayed"] = df["delayed"].astype(int)

    # 8. Sort by order date
    df = df.sort_values("orderdate")

    return df


def generate_report(
    raw_df: pd.DataFrame,
    clean_df: pd.DataFrame
) -> str:
    """Generate a basic data-quality report."""

    raw_rows = len(raw_df)
    clean_rows = len(clean_df)
    removed_rows = raw_rows - clean_rows

    report = f"""
SALES DATA QUALITY REPORT
=========================

Original rows: {raw_rows}
Clean rows: {clean_rows}
Rows removed: {removed_rows}

Original columns: {len(raw_df.columns)}
Clean columns: {len(clean_df.columns)}

Missing values after cleaning:
{clean_df.isnull().sum().to_string()}

Duplicate rows after cleaning:
{clean_df.duplicated().sum()}
"""

    return report.strip()


def main():
    """Run the complete data-cleaning pipeline."""

    print("Loading raw data...")

    raw_df = load_data(INPUT_FILE)

    print(f"Raw dataset: {raw_df.shape[0]} rows, {raw_df.shape[1]} columns")

    print("Cleaning data...")

    clean_df = clean_data(raw_df)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    clean_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    report = generate_report(
        raw_df,
        clean_df
    )

    report_file = OUTPUT_FILE.parent / "data_quality_report.txt"

    report_file.write_text(
        report,
        encoding="utf-8"
    )

    print("\nPipeline completed successfully.")
    print(f"Clean dataset: {OUTPUT_FILE}")
    print(f"Quality report: {report_file}")

    print("\nClean dataset preview:")
    print(clean_df.head().to_string(index=False))


if __name__ == "__main__":
    main()