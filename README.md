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

find a server, add this script to cronjob
