from scripts.extract import extract_from_api, extract_from_db, extract_from_csv
from scripts.transform import clean_data, aggregate_data, normalize_data
from scripts.load import load_to_redshift
import json

def main():
    # Load configurations
    with open('config/aws_config.json', 'r') as f:
        aws_config = json.load(f)
    
    # Extract
    api_url = "put_api_url_here"
    db_conn_str = "postgresql://user:password@localhost:5432/dbname"
    db_query = "SELECT * FROM your_table"
    csv_file = "data/raw/your_data.csv"
    
    df_api = extract_from_api(api_url)
    df_db = extract_from_db(db_conn_str, db_query)
    df_csv = extract_from_csv(csv_file)
    
    # Transform
    df = pd.concat([df_api, df_db, df_csv], ignore_index=True)
    df = clean_data(df)
    df = aggregate_data(df, 'category', 'sales', 'sum')
    df = normalize_data(df, ['sales'])
    
    # Load
    load_to_redshift(df, 'transformed_data', aws_config['redshift'])

if __name__ == "__main__":
    main()
