import pandas as pd
import psycopg2
import json

def load_to_redshift(df, table_name, redshift_config):
    conn = psycopg2.connect(
        dbname=redshift_config['dbname'],
        user=redshift_config['user'],
        password=redshift_config['password'],
        host=redshift_config['host'],
        port=redshift_config['port']
    )
    cursor = conn.cursor()
    
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join([f'{col} VARCHAR' for col in df.columns])}
    );
    """
    cursor.execute(create_table_query)
    
    for i, row in df.iterrows():
        insert_query = f"INSERT INTO {table_name} VALUES {tuple(row)}"
        cursor.execute(insert_query)
    
    conn.commit()
    cursor.close()
    conn.close()

# usage example
if __name__ == "__main__":
    with open('config/aws_config.json', 'r') as f:
        redshift_config = json.load(f)['redshift']
    
    df = pd.read_csv('data/transformed/transformed_data.csv')
    load_to_redshift(df, 'transformed_data', redshift_config)
