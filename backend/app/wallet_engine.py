
from web3 import Web3
from eth_account import Account
import os

RPC = os.getenv("ETH_RPC","https://rpc.ankr.com/eth")

w3 = Web3(Web3.HTTPProvider(RPC))

def create_wallet():
    acct = Account.create()

    return {
        "address": acct.address,
        "private_key": acct.key.hex()
    }
