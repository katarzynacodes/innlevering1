# først henter vi en Operating System modul. Dette fungerer som en verktøykasse som gir tilgang til verktøy/funksjoner.
# senere kommer vi til å bruke en innebygd funksjon som gjør at Python skal kunne klare å lese API-nøkkelen.  
# grunnen til at man starter med import os er beste praksis (PEP 8) samt det gir en umiddelbar oversikt over hvilke eksterne biblioteker og moduler skriptet 
# er avhengig av for å kjøre. 
import os 

# neste steg er å hente requests-biblioteket. Det muliggjør HTTP-forespørsler for å hente info om kurser. 
import requests 

# neste steg er å hente funksjonen load_dotenv fra biblioteket dotenv, som gjør at vi kan hente miljøvariabler (nøkkelen) fra systemet.
# vi bruker dotenv for å hente API-nøkkelen fra filen og lagrer den i systemet.
# vi importerer kun et verktøy og ikke hele biblioteket for å gjøre koden mer effektiv og oversiktlig.
from dotenv import load_dotenv

# etter å ha importert load_dotenv bruker vi funksjonen for å hente API-nøkkelen fra systemet.
load_dotenv()
# parentes viser at dette er en funksjon som skal kjøres. 
# funksjonen har tre oppgaver: 1. den henter .env-fil, 2. den leser innholdet og 3. den tar nøkkelen og plasserer den inn i 
# operativsystemets usynlige minne. 

# I .env-filen har vi lagret API-nøkkelen som en miljøvariabel EXCHANGE_API_KEY=...
# I neste linje skal vi hente variabelen fra systemet/filen og lagre den i en variabel api_key i terminalen.
# dette gjøres ved å bruke os-modulens funksjon getenv som henter miljøvariabler fra systemet.
api_key = os.getenv("EXCHANGE_API_KEY")
# denne linjen med andre ord lagrer api_nøkkelen i en variabel som vi kan bruke senere i koden.
# os.getenv(...) betyr "Operating System: Get Environment Variable".

# i neste steg skal vi oppgi en URL som vi skal bruke for å hente data fra Kraken. 
# URL-en er en streng som inneholder adressen til Kraken sin API for å hente kurser for utvalgte EUR-par.
kraken_url = "https://api.kraken.com/0/public/Ticker?pair=XXBTZEUR"
# I en annen fil skal jeg forklare hvordan vi lager en URL som henter krypto- og valutakurser.

# I neste linje skal jeg sende HTTP GET-forespørsel til Kraken sin API for å hente kurser for det utvalgte EUR-paret.
# jeg brukte forkortelsen res for å lagre responsen som vi fikk fra Kraken sin API.
# res er en standard konvensjon blant utviklere for å gjøre koden kort, lesbar og lett å kjenne igjen for andre utviklere.
res = requests.get(kraken_url)
# hva som skjer på denne linjen:
# requests er et bibliotek som vi importerte tidligere.
# get er en metode fra requests-biblioteket som sender en HTTP GET-forespørsel til den oppgitte URL-en (kraken_url) 
# og returnerer responsen som vi fikk fra Kraken sin API.
# res er forkortelse for response, der Python lagrer responsen som vi fikk fra Kraken sin API i en variabel res.

# i neste linje skal jeg hente JSON-data fra responsen som vi fikk fra Kraken sin API, oversette den til Python-språk og lagre den i en variabel data.
# navnet data er en standard konvensjon blant utviklere for å gjøre koden kort, lesbar og lett å kjenne igjen for andre utviklere.
# data er en ordbok som inneholder kurser og annen informasjon om de utvalgte EUR-parene.
data = res.json()

# i neste steg skal vi printe ut dataen som vi fikk fra Kraken sin API for å se hvordan den ser ut og hva den inneholder.
print(data)

# her er et eksempel på hvordan dataen ser ut som vi fikk fra Kraken sin API:
# {
# "error": [],
# "result": {
#   "XXBTZEUR": {
#     "a": ["62340.10000", "1", "1.000"],
#     "b": ["62340.00000", "2", "2.000"],
#     "c": ["62340.10000", "0.01500000"],
#     "v": ["350.12345678", "1200.87654321"],
#     "p": ["62150.45678", "61980.12345"],
#     "t": [4520, 15800],
#     "l": ["61200.00000", "60800.00000"],
#     "h": ["62800.00000", "62800.00000"],
#     "o": "61500.00000"
#   }
# }
# }
#
# I data-filen lå "error" og "result" ved siden av hverandre. 
# error er en liste over eventuelle feil som oppstod under forespørselen. Her ser vi at listen er tom, noe som betyr at både forespørsel og svar er gyldig. 
# result er en ordbok som inneholder kurser og annen informasjon om EUR-parene.

# videre skal vi hente ut kun kursene og lagre det i resultat-ordboken. 
resultat = data["result"]
# forskjellen mellom data og resultat er at data inneholder både error og resultat, mens resultat kun inneholder kurser og annen informasjon om EUR-parene.
# data["result"] betyr at vi henter ut verdien som er lagret i nøkkelen "result" i data-ordboken og lagrer den i variabelen resultat. 

# ok, i neste steg skal vi hente ut pris for et spesifikt par, for eksempel BTC/EUR. Vi kan gjøre dette ved å bruke resultat-ordboken som vi hentet ut tidligere. 
# Vi kan hente ut kursen for BTC/EUR ved å bruke nøkkelen "XXBTZEUR" som er lagret i resultat-ordboken.
btc_pris_euro = resultat["XXBTZEUR"]["c"][0]

# hva som skjer i denne linjen:
# resultat["XXBTZEUR"] betyr at vi henter ut verdien som er lagret under nøkkelen "XXBTZEUR" i resultat-ordboken.
# ["c"] betyr at vi henter ut verdien som er lagret under nøkkelen "c" i ordboken som er lagret under nøkkelen "XXBTZEUR".
# [0] henter ut den første verdien i listeelementet, som er selve siste pris.

# i neste steg skal vi printe ut kursen for BTC/EUR. 
print("Siste pris for BTC/EUR:", btc_pris_euro)
# print(btc_pris_euro) printer ut verdien som er lagret i variabelen.
# derfor legger vi til en forklarende tekst (Siste pris for BTC/EUR:) for å gjøre det mer forståelig for brukeren.

# verdien er lagret som datatype string. For å kunne gange den med et tall må vi konvertere den til en float. 
btc_pris_euro_float = float(btc_pris_euro) 

# bra, neste steg er å hente ut valutakursen for NOK/EUR. 
# vi har allerede hentet ut API-nøkkelen og lagret den i variabelen api_key. Nå skal vi bruke den til å hente ut valutakursen for NOK/EUR fra en annen API.
# Her setter vi sammen URL-en ved hjelp av en f-streng (f"{api_key}"), som setter inn den faktiske API-nøkkelen vår direkte i nettadressen.
exchange_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"

# i neste linje sender vi en HTTP GET-forespørsel til ExchangeRate-API for å hente ned valutakursene.
# vi bruker forkortelsen res_ex (response exchange) for å skille denne responsen fra den vi fikk fra Kraken tidligere.
res_ex = requests.get(exchange_url)

# deretter henter vi ut JSON-dataen fra responsen og oversetter den til et Python-format, akkurat som vi gjorde med Kraken.
# data_ex er en ordbok som inneholder all informasjon om valutakursene, der "ex" står for exchange.
data_ex = res_ex.json()

# i denne linjen henter vi ut selve valutakursen for NOK fra ordboken.
# data_ex["conversion_rates"] går inn i nøkkelen som inneholder alle kursene, og ["NOK"] henter ut tallverdien for norske kroner.
nok = data_ex["conversion_rates"]["NOK"] 

# her printer vi ut valutakursen for NOK/EUR i terminalen slik at vi kan se hva én Euro er verdt i norske kroner.
print("Valutakurs for NOK/EUR:", nok)

# akkurat som med kryptoprisen er valutakursen hentet inn som en tekststreng (string). 
# For å kunne utføre matematiske utregninger (ganging) må vi konvertere denne verdien til et desimaltall ved hjelp av float().
nok_float = float(nok)

# i denne linjen regner vi ut prisen på Bitcoin i norske kroner.
# vi tar desimaltallet for Bitcoin i euro (btc_pris_euro_float) og ganger det med desimaltallet for valutakursen (nok_float).
btc_pris_nok = btc_pris_euro_float * nok_float 

# til slutt printer vi ut det endelige resultatet i terminalen: den omregnede prisen for Bitcoin i NOK.
# vi legger til en forklarende tekst (Siste pris for BTC/NOK:) slik at det blir lett for brukeren å lese av svaret.
print("Siste pris for BTC/NOK:", btc_pris_nok)