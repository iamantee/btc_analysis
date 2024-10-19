import pandas as pd

def read_csv_to_dataframe(file_path):
    """
    Read a CSV file into a pandas DataFrame.
    
    Args:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(file_path, parse_dates=['timestamp'], index_col='timestamp')
    return df

def calculate_coinbase_premium(coinbase_df, binance_df):
    """
    Calculate the Coinbase premium gap between Coinbase price (BTCUSD) and Binance price (BTCUSDT).
    
    Args:
    coinbase_df (pd.DataFrame): DataFrame containing Coinbase price data.
    binance_df (pd.DataFrame): DataFrame containing Binance price data.
    
    Returns:
    pd.DataFrame: A DataFrame with the calculated Coinbase premium.
    """
    # Ensure both DataFrames have the same index
    common_index = coinbase_df.index.intersection(binance_df.index)
    coinbase_df = coinbase_df.loc[common_index]
    binance_df = binance_df.loc[common_index]
    
    # Calculate the premium using the 'close' price
    premium = coinbase_df['close'] - binance_df['close']
    
    # Create a new DataFrame with the premium
    premium_df = pd.DataFrame({'coinbase_premium': premium})
    
    return premium_df

def standardize_coinbase_premium(premium_df):
    """
    Standardize the Coinbase premium gap.
    
    Args:
    premium_df (pd.DataFrame): DataFrame containing the Coinbase premium data.
    
    Returns:
    pd.DataFrame: A DataFrame with the standardized Coinbase premium.
    """
    # Calculate mean and standard deviation of the premium
    mean_premium = premium_df['coinbase_premium'].mean()
    std_premium = premium_df['coinbase_premium'].std()
    
    # Standardize the premium
    standardized_premium = (premium_df['coinbase_premium'] - mean_premium) / std_premium
    
    # Add the standardized premium to the DataFrame
    premium_df['standardized_premium'] = standardized_premium
    
    return premium_df

def merge_and_calculate_premium(binance_file, coinbase_file):
    """
    Read CSV files, merge dataframes, calculate and standardize Coinbase premium.
    
    Args:
    binance_file (str): Path to the Binance CSV file.
    coinbase_file (str): Path to the Coinbase CSV file.
    
    Returns:
    pd.DataFrame: A merged DataFrame with calculated premiums.
    """
    # Read CSV files
    binance_df = read_csv_to_dataframe(binance_file)
    coinbase_df = read_csv_to_dataframe(coinbase_file)
    
    # Calculate Coinbase premium
    premium_df = calculate_coinbase_premium(coinbase_df, binance_df)
    
    # Standardize Coinbase premium
    premium_df = standardize_coinbase_premium(premium_df)
    
    # Merge dataframes
    merged_df = binance_df.join(coinbase_df, lsuffix='_binance', rsuffix='_coinbase')
    
    # Add premium columns
    merged_df['cb_gap'] = premium_df['coinbase_premium']
    merged_df['std_cb_gap'] = premium_df['standardized_premium']
    
    return merged_df

# Perform the analysis
merged_data = merge_and_calculate_premium('binance_btcusdt_data.csv', 'coinbase_btcusdt_data.csv')
selected_columns = ['timestamp', 'close_binance', 'volume_binance', 'close_coinbase', 'volume_coinbase', 'cb_gap', 'std_cb_gap']
merged_data[selected_columns].to_csv('cb_premium_data_cleaned.csv', index=False)
