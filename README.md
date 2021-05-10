FTX Lending Bot
===

Renew margin lending amount.

![demo](/img/demo.png)

## Setup

please use Python 3.7+

```
pip install -r requirements.txt
```

copy `.env.sample` to `.env` and add your API key and secret

## Usage

Show usage:

```bash
python main.py -h
```

Example:

```bash
python main.py -a "My Sub-Account" -c "USDT" -r "1e-6"
```

## Automatically renew

### Use GitHub Action

- clone this repo
- add `FTX_API` and `FTX_API_SECRET` to repo > settings > secret.
- modify the sub-account, coin and lending rate in `.github/workflows/cron.yml`

## Disclaimer

Do not upload / commit your API key and secret to internet! Keep them in private.
