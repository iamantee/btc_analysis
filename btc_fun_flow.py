import pandas as pd
import numpy as np

def calculate_btc_fun_flow(transactions_df, exchange_inflows_df):
    """
    Calculate the BTC Fun Flow metric.

    Args:
    transactions_df (pd.DataFrame): DataFrame containing all BTC transactions.
    exchange_inflows_df (pd.DataFrame): DataFrame containing BTC inflows to exchanges.

    Returns:
    pd.DataFrame: A DataFrame with the calculated BTC Fun Flow metric.
    """
    # Group transactions by timestamp and sort by total BTC sent
    grouped_transactions = transactions_df.groupby('timestamp').apply(
        lambda x: x.nlargest(10, 'btc_amount')
    ).reset_index(drop=True)

    # Calculate the sum of top 10 transactions for each timestamp
    top_10_sum = grouped_transactions.groupby('timestamp')['btc_amount'].sum()

    # Calculate total inflows for each exchange
    total_inflows = exchange_inflows_df.groupby('timestamp')['btc_amount'].sum()

    # Calculate BTC Fun Flow metric
    btc_fun_flow = top_10_sum / total_inflows

    # Create a DataFrame with the results
    result_df = pd.DataFrame({
        'timestamp': btc_fun_flow.index,
        'btc_fun_flow': btc_fun_flow.values
    })

    return result_df

# Example usage (assuming you have the necessary DataFrames):
# transactions_df = pd.read_csv('btc_transactions.csv')
# exchange_inflows_df = pd.read_csv('exchange_inflows.csv')
# btc_fun_flow_df = calculate_btc_fun_flow(transactions_df, exchange_inflows_df)
# btc_fun_flow_df.to_csv('btc_fun_flow_metric.csv', index=False)




