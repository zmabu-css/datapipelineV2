import pandas as pd

def clean_data(df):
    df.dropna(inplace=True)
    return df

def aggregate_data(df, group_by_column, aggregation_column, agg_func='sum'):
    return df.groupby(group_by_column)[aggregation_column].agg(agg_func).reset_index()

def normalize_data(df, columns):
    for column in columns:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df

# for examples
if __name__ == "__main__":
    df = pd.read_csv('data/raw/api_data.csv')
    df = clean_data(df)
    df = aggregate_data(df, 'category', 'sales', 'sum')
    df = normalize_data(df, ['sales'])
    
    # Save transformed data
    df.to_csv('data/transformed/transformed_data.csv', index=False)
