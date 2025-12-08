#This script loads raw sales data, cleans it, and remove invalid entries. The purpose is to ensure the dataset is ready to be analysed.
import pandas as pd

# Load the raw CSV file into a pandas DataFrame
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df

# Clean Column Names by :
# 1. Removing leading & trailing spaces 
# 2. Turning owercase 
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

#Handle Missing values by
#1. Drop rows with missing price
#2. Fill missing values in the quanitity column with 0
def handle_missing_values(df):
    df = df.dropna(subset=['price', 'date_sold'])          
    df['qty'] = df['qty'].fillna(0)          
    return df
    

#1. Columns 'prodname' & 'category' should be striped from leading/trailing spaces and have title case
#2. Remove negative value in columns 'price' and 'qty'
def remove_invalid_rows(df):
    df['prodname'] = df['prodname'].str.strip().str.title()
    df['category'] = df['category'].str.strip().str.title()

    #Change data to numerical 
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df = df[(df['qty'] >= 0) & (df['price'] >= 0)]
    
    return df


if __name__ == "__main__":
    raw_path = "../data/raw/sales_data_raw.csv"
    cleaned_path = "../data/processed/sales_data_clean.csv"


    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    
    print("Cleaning complete. First few rows:")
    print(df_clean.head())


