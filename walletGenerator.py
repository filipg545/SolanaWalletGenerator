import base58
from solders.keypair import Keypair

while True:
    try:
        walletAmount = int(input('How many wallets do you want? ').strip())
        break
    except Exception:
        continue

for x in range(walletAmount):
    account = Keypair()
    privateKey = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')

    print(f'{x + 1}. Wallet Address: {account.pubkey()}')
    print(f'{x + 1}. Private Key: {privateKey}')