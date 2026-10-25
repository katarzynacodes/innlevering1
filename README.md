# Bitcoin til NOK Konverter (Kraken & ExchangeRate API)

Dette prosjektet er et Python-program som henter sanntidsprisen på Bitcoin (BTC) i Euro (EUR) fra Kraken sin API, henter den nyeste valutakursen mellom EUR og NOK fra ExchangeRate-API, og regner om prisen slik at du får verdien av Bitcoin direkte i norske kroner (NOK).

Prosjektet er utviklet som en del av semesteroppgaven.

---

## Om prosjektet og bakgrunn

I denne oppgaven valgte jeg å lage en kode som tillater å gjøre om kryptokurser i Euro til NOK. Personlig bruker jeg Kraken kryptobørs fordi den har et mye større utvalg av krypto, samt at gebyrene er mye lavere enn hos norske børser som Firi. 

Kraken er en internasjonal børs som opererer i USD og EUR. Likevel har jeg en bedre følelse når jeg opererer med NOK som utgangspunkt. Jeg starter med et utvalg av kryptovalutaer (Bitcoin i dette eksempelet), selv om Kraken har over 200 kryptovalutaer tilgjengelige. Videre skal jeg utvide koden med flere kryptovalutaer, analyser og automatisert trading-bot. 

---

## API-kilder og oppbygging av URL-er

Programmet benytter seg av to API-er:

### 1. Kraken API (Markedsdata for Bitcoin)
For å hente sanntidskurs for Bitcoin i Euro benyttes Kraken sitt REST API.

**Hvordan URL-en ble oppbygd ut fra dokumentasjonen:**
1. I Kraken API-dokumentasjonen (*Exchange API reference*) under *Markets Base URL (REST)* finner vi domenet for Spot: `https://api.kraken.com`. Vi velger REST fordi tilkoblingsmodellen er basert på request/response (forespørsel/svar). Portnummeret rutes automatisk til port 443 siden den bruker HTTPS.
2. Under workflows leser vi at markedsdata fungerer på offentlige endepunkter, så **ingen API-nøkkel er nødvendig** for å lese dette.
3. Fast sti for offentlige funksjoner er `/0/public/`.
4. Endepunktet for sanntidspris (*Ticker*) legges til: `/Ticker`.
5. For å hente prisen på et spesifikt par mot Euro benyttes parameteren `pair=XXBTZEUR` (som er Kraken sine interne symboler for Bitcoin og Euro).

**Endelig URL:**
`https://api.kraken.com/0/public/Ticker?pair=XXBTZEUR`

---

### 2. ExchangeRate-API (Valutakurs EUR til NOK)
For å regne om Euro til norske kroner benyttes ExchangeRate-API, da denne tjenesten tilbyr en enkel og gratis løsning for valutakursdata.

**Sikkerhet og autentisering:**
* Denne API-en **krever en personlig API-nøkkel**.
* Nøkkelen lagres trygt i en lokal `.env`-fil under variabelnavnet `EXCHANGE_API_KEY` for å forhindre at følsomme opplysninger blir publisert offentlig på GitHub.

**Hvordan URL-en er strukturert:**
Ut fra dokumentasjonen er GET-forespørsler strukturert som følger:
`https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/EUR`

Når API-nøkkelen hentes dynamisk fra miljøvariablene, blir URL-en i koden:
`https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR`

Ved hjelp av GET-metoden henter koden ut en JSON-pakke, hvor vi leser av verdien plassert under `conversion_rates["NOK"]`.

---

## Forutsetninger og Krav

For å kjøre dette programmet må du ha følgende installert på maskinen din:
* **Python 3.x**
* Følgende Python-biblioteker:
  * `requests`
  * `python-dotenv`

---

## Installasjon og Oppsett

Følg disse stegene for å kjøre prosjektet lokalt:

### 1. Kloning av lageret
Klon dette GitHub-lageret til din maskin:
```bash
git clone https://github.com/katarzynacodes/innlevering1.git
cd innlevering1 
```

### 2. Installer nødvendige biblioteker
Kjør følgende kommando i terminalen for å installere bibliotekene:
```bash
pip install requests python-dotenv
```

### 3. Skaff en API-nøkkel
1. Gå til [ExchangeRate-API](https://www.exchangerate-api.com/) og opprett en gratis konto.
2. Kopier din personlige API-nøkkel fra dashbordet.

### 4. Opprett `.env`-fil
Opprett en fil med navnet `.env` i rotmappen til prosjektet (på samme sted som Python-filen din) og legg inn API-nøkkelen din slik:

```env
EXCHANGE_API_KEY=din_faktiske_api_nøkkel_her
```

> **Merk:** `.env`-filen skal **ikke** legges til i Git eller publiseres på GitHub. Sørg for at den ligger i `.gitignore`.

---

## Hvordan kjøre programmet

Når `.env`-filen er opprettet og bibliotekene er installert, kan du kjøre skriptet fra terminalen:

```bash
python min_kode.py
```


### Forventet resultat i terminalen:
Programmet vil hente data og skrive ut blant annet:
```text
Siste pris for BTC/EUR: 62340.10000
Valutakurs for NOK/EUR: 11.65
Siste pris for BTC/NOK: 726262.165
```