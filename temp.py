import requests
import json

def get_latest_block():
    url = "https://api.blockcypher.com/v1/btc/main"
    response = requests.get(url)
    
    if response.status_code == 200:
        latest_block = response.json()['height']
        return latest_block
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def get_block_data(block_height):
    url = f"https://api.blockcypher.com/v1/btc/main/blocks/{block_height}"
    response = requests.get(url)
    
    if response.status_code == 200:
        block_data = response.json()
        return block_data
    else:
        print(f"Failed to retrieve block data for height {block_height}: {response.status_code}")
        return None

# Get the latest block height
latest_block_height = get_latest_block()
if latest_block_height:
    print(f"Latest Block Height: {latest_block_height}")
    
    # Fetch data for the latest block
    block_info = get_block_data(latest_block_height)
    if block_info:

        print("Block Info:")
        print(json.dumps(block_info, indent=4, sort_keys=True))

        print(f"Block Hash: {block_info['hash']}, Time: {block_info['time']}")
        print(f"Transactions: {len(block_info['txids'])}")
