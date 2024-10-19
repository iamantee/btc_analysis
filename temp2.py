import requests
import time

def get_btc_balance(address):
    url = f"https://blockchain.info/q/addressbalance/{address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Balance is returned in satoshis, convert to BTC
        balance_satoshis = int(response.text)
        balance_btc = balance_satoshis / 100000000  # 1 BTC = 100,000,000 satoshis

        print(f"Balance of {address}: {balance_btc:.8f} BTC")

        return balance_btc
    else:
        print(f"Failed to retrieve balance: {response.status_code}")
        return None

# Example usage
btc_address_arr = [
    "1PJiGp2yDLvUgqeBsuZVCBADArNsk6XEiw",
    "1Pzaqw98PeRfyHypfqyEgg5yycJRsENrE7",
    "32KqbtrRVxC6GLUJgJhVQtFTaCdq4GrgBb",
    "32bhzEniykYRFADVaRM5PYswsjC23cxtes",
    "34GUzCVLbdkMQ2UdVTaA4nxPwoovVS7y2J",
    "34HpHYiyQwg69gFmCq2BGHjF1DZnZnBeBP",
    "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo",
    "36zSLdRv1jyewjaC12fqK5fptn7PqewunL",
    "38DN2uFMZPiHLHJigfv4kWC9JWJrNnhLcn",
    "38Xnrq8MZiKmYmwobbYdZQ5nnCbX1qvQfE",
    "395vnFScKQ1ay695C6v7gf89UzoFpx3WuJ",
    "39884E3j6KZj82FK4vcCrkUvWYL5MQaS3v",
    "3AQ8bAh88TQU7JV1H3ovXrwsuV6s3zYZuN",
    "3AeUiDpPPUrUBS377584sFCpx8KLfpX9Ry",
    "3AtnehKDkFPC1bKvdrEVPSRGCtxQH8F1R8",
    "3CySuFKbBS29M7rE5iJakZRNqb3msMeFoN",
    "3E97AjYaCq9QYnfFMtBCYiCEsN956Rvpj2",
    "3EVVc8e2rxwUuERtdJCduWig8DnpsUqyA6",
    "3F9CGMu7JSJnMHA8jFM2KgxuH6hhxtvENP",
    "3FHNBLobJnbCTFTVakh5TXmEneyf5PT61B",
    "3HdGoUTbcztBnS7UzY4vSPYhwr424CiWAA",
    "3JFJPpH8Chwo7CDbyYQ4XcfgcjEP1FGRMJ",
    "3JJmF63ifcamPLiAmLgG96RA599yNtY3EQ",
    "3JqPhvKkAPcFB3oLELBT7z2tQdjpnxuDi9",
    "3Jy7A2rThtU9xm4o8gR3a9pvQuxXnRNuNF",
    "3LQUu4v9z6KNch71j7kbj8GPeAGUo1FW6a",
    "3LcgLHzTvjLKBixBvkKGiadtiw2GBSKKqH",
    "3LtrsjtyLsHoG8WQMe2RFw3de4pLTQZNcY",
    "3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6",
    "3Me9QACjioepv2L2oKTC9QQ87NH6vFe1Zj",
    "3NPL82eaehTFh4r3StpHqVQBTnZJFaGsyy",
    "3NXCvmLGz9SxYi6TnjbBQfQMcwiZ1iQETa",
    "3NjHh71XgjikBoTNYdWgXiNeZcLaKNThgb",
    "3PXBET2GrTwCamkeDzKCx8DeGDyrbuGKoc",
    "3QK5vQ9hucSg8ZC8Vizq83qEWeHFLAWMud",
    "3Qxak1CZhLyZ7GVckKphLURdLBCjMfz9bA",
    "bc1q32lyrhp9zpww22phqjwwmelta0c8a5q990ghs6",
    "bc1q78ufzeu8w8fwvxuphrdlg446xhyptf28fkatu5",
    "bc1q7t9fxfaakmtk8pj7tdxjvwsng6y9x76czuaf5h",
    "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h",
    "bc1qq393eyjh8hdjvcchy0mxquhh9wx8h3kzlkchfs"] 

balance = []

total_balance = 0

for btc_address in btc_address_arr:
    time.sleep(1)
    balance.append(get_btc_balance(btc_address))
    total_balance += balance[-1]

if balance is not None:
    print(balance)


