(Archived) Farewell FTX.
===

![FhDdJpZakAEw81E](https://user-images.githubusercontent.com/31836528/200633079-ac34c1c1-624c-4591-9d5b-7db7bfb9ad50.jpeg)


---
FTX Lending Bot
===

Renew margin lending amount.

![demo](/img/demo.png)

## Note for who want to fork this repo

- I have change the default lending coin to USD in https://github.com/dwy6626/ftx-lending-bot/commit/ffc7f74a9138a4191677127f96d874bd44885952, there might be more changes on master branch in future. you can use the released version (currently is v1.1) which is more stable.

## Usage

Show usage:

```bash
python main.py -h
```

Example:

```bash
python main.py -a "My Sub-Account" -c "USDT" -r "1e-6"
```

## Local Setup

please use Python 3.7+

```
pip install -r requirements.txt
```

copy `.env.sample` to `.env` and add your API key and secret

## Automatically renew

### Use GitHub Action

- clone this repo
- add `FTX_API` and `FTX_API_SECRET` to repo > settings > secret.
- modify the sub-account, coin and lending rate in `.github/workflows/cron.yml`

### Disable Renew Schedules

Manual dispatch the workflow `disable.yml` on GitHub website.

### Re-enable

Because scheduled workflow are automatically disabled after 60 days inactivity, there is another workflow `reenable.yml` run monthly to automatically re-enable the workflows

This workflow also provides manual dispatch on GitHub website for re-enabling.

## Disclaimer

Do not upload / commit your API key and secret to internet! Keep them in private.
