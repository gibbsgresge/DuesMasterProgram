from sqlalchemy import create_engine
import pandas as pd

def fetch_data():
    # Database connection details
    host = "00" 
    dbname = "zete_dues_and_fine"
    user = "root"
    password = "mypassword"

    # Create an SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{dbname}")

    # SQL query
    sql_query = "SELECT * FROM brothersspring2024"

    # Fetch the data using the engine
    data = pd.read_sql(sql_query, engine)

    return data

# This if-block ensures the script only executes when run directly, not when imported
if __name__ == "__main__":
    data = fetch_data()
    print(data)  # Print the first few rows for testing
