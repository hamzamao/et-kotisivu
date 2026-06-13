# ET Digiapu & Digiturva – kotisivut

Staattinen kotisivusto digiapupalvelulle: kotikäyntejä senioreille (puhelin,
netti, TV, turvallinen asiointi) sekä **Digiturva-jäsenyys** – huijausvahti, jossa
asiakas lähettää kuvakaappauksen epäilyttävästä viestistä ja saa vastauksen.
Moderni ulkoasu (Inter-fontti, gradienttihero, kortit), mutta luettavuus edellä:
iso teksti, vahva kontrasti, suuret painikkeet. Ei build-vaihetta eikä
riippuvuuksia – pelkkää HTML:ää ja CSS:ää.

## Sivut

| Tiedosto           | Sisältö                                                  |
| ------------------ | -------------------------------------------------------- |
| `index.html`       | Etusivu: kotikäynnit + Digiturva-nosto + näin se toimii   |
| `palvelut.html`    | Kotikäyntipalvelut kiinteillä hinnoilla                   |
| `digiturva.html`   | Huijausvahti + jäsenyystasot 24,90 € / 39,90 € + UKK      |
| `hinnat.html`      | Hinnasto, jäsenyydet ja kotitalousvähennys                |
| `lahjakortti.html` | Lahjakortit (kohderyhmänä aikuiset lapset)                |
| `minusta.html`     | Esittely, kasvokuva, lupaukset asiakkaalle                |
| `yhteys.html`      | Puhelin, soittopyyntölomake, palvelualue                  |

Ylä- ja alatunniste on kopioitu jokaiselle sivulle, koska sivustolla ei ole
build-vaihetta. Jos muutat valikkoa tai alatunnistetta, muuta kaikkiin
seitsemään tiedostoon.

## Tärkeää: miten "tekoälyhuijaustarkistus" oikeasti toimii

Tämä on **staattinen sivusto** (esim. GitHub Pages), joten se ei voi itse ajaa
tekoälyä turvallisesti – API-avain paljastuisi kävijöille. Siksi sivusto kuvaa
palvelun näin: **asiakas lähettää kuvakaappauksen WhatsAppilla → tekoäly
analysoi → sinä varmistat tuloksen ihmisenä → vastaat.** Tämä toimii heti, kun
sinä olet mukana silmukassa, ja se on myös myyntivaltti ("ihminen ratkaisee,
ei botti").

Kun haluat automatisoida analyysin, tarvitaan pieni taustapalvelin (esim. yksi
serverless-funktio Cloudflare Workersissa tai Vercelissä), joka kutsuu
kuva-analyysin tekevää tekoälymallia. Avain pidetään palvelimella, ei sivulla.
Tämä on luonteva seuraava vaihe – ei tarpeen julkaisua varten.

## Ennen julkaisua: täytä paikkamerkit

Etsi ja korvaa kaikista `.html`-tiedostoista:

- [ ] **`Etunimi Sukunimi`** → oma nimesi
- [ ] **`[Kaupunki]`** → palvelualueesi
- [ ] **`[0000000-0]`** → oikea Y-tunnus
- [ ] **`040 123 4567`** / **`+358401234567`** / **`358401234567`** → oikea numero
      (näkyvä teksti, `tel:`-linkit, WhatsApp-linkit `wa.me`, JSON-LD)
- [ ] **`info@etdigiapu.fi`** ja **`https://www.etdigiapu.fi/`** → oikea sähköposti ja domain
- [ ] **Hinnat** – tarkista kertahinnat (79–149 €) ja jäsenmaksut (24,90 / 39,90 €)
- [ ] **`img/kasvokuva.svg`** → oikea kasvokuva (`minusta.html`)
- [ ] **Soittopyyntölomake** (`yhteys.html`) – luo lomake [formspree.io](https://formspree.io)-palvelussa ja korvaa `LOMAKETUNNUS`
- [ ] **Kotitalousvähennys** (`hinnat.html`) – varmista summat ja prosentti [vero.fi](https://www.vero.fi)
- [ ] **Digiturva-numero** – päätä, onko se sama puhelinnumero vai erillinen WhatsApp

## Julkaisu GitHub Pagesissa

1. **Settings → Pages → Source: Deploy from a branch**, valitse haara ja `/ (root)`.
2. Sivusto ilmestyy osoitteeseen `https://<käyttäjä>.github.io/et-kotisivu/`.
3. Oma domain: osta tunnus, lisää se Pagesin asetuksiin ja tee nimipalveluun
   ohjeiden mukaiset tietueet.

## Paikallinen esikatselu

```sh
python3 -m http.server 8000
```
ja avaa <http://localhost:8000>.
