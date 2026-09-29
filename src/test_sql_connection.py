import mssql_python


SERVER = r"DESKTOP-RJ120V4\SQL2025EDE"
DATABASE = "SalesDataPipeline"


def main():
    connection_string = (
        f"Server={SERVER};"
        f"Database={DATABASE};"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    try:
        with mssql_python.connect(connection_string) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    DB_NAME() AS DatabaseName,
                    @@SERVERNAME AS ServerName
            """)

            row = cursor.fetchone()

            print("Connection successful!")
            print(f"Server: {row.ServerName}")
            print(f"Database: {row.DatabaseName}")

    except Exception as error:
        print("Connection failed.")
        print(error)


if __name__ == "__main__":
    main()