import requests
import pandas as pd

def extract_from_api(url):
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

def extract_from_db(connection_string, query):
    import sqlalchemy
    engine = sqlalchemy.create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df

def extract_from_csv(file_path):
    return pd.read_csv(file_path)

# usage example
if __name__ == "__main__":
    api_url = "YOUR_API_URL"
    db_conn_str = "postgresql://user:password@localhost:5432/dbname"
    db_query = "SELECT * FROM your_table"
    csv_file = "data/raw/your_data.csv"
    
    df_api = extract_from_api(api_url)
    df_db = extract_from_db(db_conn_str, db_query)
    df_csv = extract_from_csv(csv_file)
    
    # saving the raw data
    df_api.to_csv('data/raw/api_data.csv', index=False)
    df_db.to_csv('data/raw/db_data.csv', index=False)
    df_csv.to_csv('data/raw/csv_data.csv', index=False)
