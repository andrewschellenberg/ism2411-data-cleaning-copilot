#This script loads raw sales data, cleans it, and remove invalid entries. The purpose is to ensure the dataset is ready to be analysed.
import pandas as pd

# Load the raw CSV file into a pandas DataFrame
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df

# Clean Column Names by :
# 1. Removing leading & trailing spaces 
# 2. Turning owercase 
#Why: Standarized column name format makes the data set easier to work with 
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

#Handle Missing values by
#1. Drop rows with missing value in column 'price', 'qty' and 'date_sold'
#Why: Missing results would make analysis results inacurate
def handle_missing_values(df):
    df = df[df['date_sold'] != '   ']
    df = df.dropna(subset=['price', 'qty'])          
    return df
    
#Remove Inavlid Rows by
#1. Removing rows with negative values or 0 values in columns 'price' and 'qty'
#Why: Negative Values can distort analysis results
def remove_invalid_rows(df):
    #Change data to numerical 
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df = df[(df['qty'] > 0) & (df['price'] > 0)]
    
    return df

#Standardize Text by
#1. Columns 'prodname' & 'category' should be striped from leading/trailing spaces and have title case
#2. Get rid of spaces inbetween product names by splitting and then joining them 
#Why: Standardiozed text makes the data easier to work with and analysis
def standarize_text(df):
    df['prodname'] = df['prodname'].str.strip().str.title()
    df['category'] = df['category'].str.strip().str.title()
    df['prodname'] = df['prodname'].str.split().str.join(' ')
    
    return df

if __name__ == "__main__":
    raw_path = "../data/raw/sales_data_raw.csv"
    cleaned_path = "../data/processed/sales_data_clean.csv"


    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean = standarize_text(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    
    print("Cleaning complete. First few rows:")
    print(df_clean.head())


