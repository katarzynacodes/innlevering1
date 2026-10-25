
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EXCHANGE_API_KEY")
kraken_url = "https://api.kraken.com/0/public/Ticker?pair=XXBTZEUR"
res = requests.get(kraken_url)
data = res.json()

print(data)

resultat = data["result"]

btc_pris_euro = resultat["XXBTZEUR"]["c"][0]
print("Siste pris for BTC/EUR:", btc_pris_euro)

btc_pris_euro_float = float(btc_pris_euro)

exchange_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"
res_ex = requests.get(exchange_url)
data_ex = res_ex.json()

nok = data_ex["conversion_rates"]["NOK"]
print("Valutakurs for NOK/EUR:", nok)

nok_float = float(nok)

btc_pris_nok = btc_pris_euro_float * nok_float
print("Siste pris for BTC/NOK:", btc_pris_nok)