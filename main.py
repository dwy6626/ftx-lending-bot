import os
import base64


from dotenv import load_dotenv
import ccxt


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    load_dotenv()

    API_KEY = os.getenv('FTX_API')
    APY_SECRET = os.getenv('FTX_API_SECRET')

    subaccount = 'Lending Bot'
    coin = 'USDT'
    rate = 1e-5

    config = {
        'apiKey': API_KEY,
        'secret': APY_SECRET,
    }

    if subaccount is not None:
        config['headers'] = { 'FTX-SUBACCOUNT': subaccount }

    client = ccxt.ftx(config)

    # get balance
    balances = client.fetch_balance()
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
        "rate": rate
    }
    res = client.private_post_spot_margin_offers(body)
    if not res['success']:
        print(res.json())
        raise Exception('lending fail')
