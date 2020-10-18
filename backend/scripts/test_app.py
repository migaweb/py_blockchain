import time
import requests
from backend.wallet.wallet import Wallet

base_url = 'http://localhost:5000'


def get_blockchain():
    return requests.get(f'{base_url}/blockchain').json()


def get_blockchain_mine():
    return requests.get(f'{base_url}/blockchain/mine').json()


def post_wallet_transact(recipient, amount):
    return requests.post(
        f'{base_url}/wallet/transact',
        json={'recipient': recipient, 'amount': amount}
    ).json()


def get_wallet_info():
    return requests.get(f'{base_url}/wallet/info').json()


start_blockchain = get_blockchain()
print(f'start_blockchain: {start_blockchain}')
recipient = Wallet().address

post_wallet_transact_1 = post_wallet_transact(recipient, 12)
print(f'\n post_wallet_transact_1: {post_wallet_transact_1}')

time.sleep(1)

post_wallet_transact_2 = post_wallet_transact(recipient, 17)
print(f'\n post_wallet_transact_2: {post_wallet_transact_2}')

time.sleep(1)

mined_block = get_blockchain_mine()
print(f'\n mined_block: {mined_block}')

wallet_info = get_wallet_info()
print(f'\nwallet_info: {wallet_info}')
