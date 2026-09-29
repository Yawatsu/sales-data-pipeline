import pandas as pd
import mssql_python
from pathlib import Path


INPUT_FILE = Path("output/sales_clean.csv")

SERVER = r"DESKTOP-RJ120V4\SQL2025EDE"
DATABASE = "SalesDataPipeline"


def load_csv() -> pd.DataFrame:
    """Load the cleaned sales dataset."""
    df = pd.read_csv(INPUT_FILE)

    # Convert date column to Python date objects
    df["orderdate"] = pd.to_datetime(
        df["orderdate"],
        errors="raise"
    ).dt.date

    return df


def get_connection():
    """Create a connection to SQL Server."""
    connection_string = (
        f"Server={SERVER};"
        f"Database={DATABASE};"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return mssql_python.connect(connection_string)


def load_to_sql(df: pd.DataFrame):
    """Load the dataframe into dbo.Sales."""

    sql = """
        INSERT INTO dbo.Sales
        (
            OrderID,
            OrderDate,
            Month,
            Region,
            Category,
            Channel,
            UnitPrice,
            Quantity,
            Revenue,
            DeliveryDays,
            Delayed,
            CustomerID,
            ChurnRisk
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    records = list(
        df[
            [
                "orderid",
                "orderdate",
                "month",
                "region",
                "category",
                "channel",
                "unitprice",
                "quantity",
                "revenue",
                "deliverydays",
                "delayed",
                "customerid",
                "churnrisk"
            ]
        ].itertuples(index=False, name=None)
    )

    with get_connection() as conn:
        cursor = conn.cursor()

        # Clear previous data so the pipeline can be rerun safely.
        cursor.execute("TRUNCATE TABLE dbo.Sales")

        cursor.executemany(sql, records)

        conn.commit()

        print(f"Successfully loaded {len(records):,} records into dbo.Sales")


def main():
    print("Loading cleaned data...")
    
    df = load_csv()

    print(f"Records ready for loading: {len(df):,}")

    load_to_sql(df)

    print("SQL loading completed successfully.")


if __name__ == "__main__":
    main()