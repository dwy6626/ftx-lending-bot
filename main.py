import os
import argparse


from dotenv import load_dotenv
import ccxt


load_dotenv()

API_KEY = os.getenv('FTX_API')
APY_SECRET = os.getenv('FTX_API_SECRET')


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--account', help='set subaccount, by default it use main account', default=None)
parser.add_argument('-c', '--coin', help='set coin to lend, default is USDT', default='USDT')
parser.add_argument('-r', '--rate', help='set lowest lending hour rate', default=1e-5)  # ~ 8.76 % / year


if __name__ == '__main__':
    args = parser.parse_args()

    config = {
        'apiKey': API_KEY,
        'secret': APY_SECRET,
    }

    subaccount = args.account
    if subaccount is not None:
        config['headers'] = { 'FTX-SUBACCOUNT': subaccount }

    client = ccxt.ftx(config)

    # get balance
    balances = client.fetch_balance()
    coin = args.coin
    for item in balances['info']['result']:
        if item['coin'] == coin:
            balance = item['total']
            break
    else:
        print(balances)
        raise Exception(f'result not found for {coin}')

    # renew lending
    body = {
        "coin": coin,
        "size": balance,
        "rate": args.rate
    }
    res = client.private_post_spot_margin_offers(body)
    if not res['success']:
        print(res.json())
        raise Exception('lending fail')
