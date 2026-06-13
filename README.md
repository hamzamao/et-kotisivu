# eTuki – kotisivut

Staattinen kotisivusto digiapupalvelulle. Kaksi tuotetta: **kotikäynnit**
senioreille (puhelin, netti, TV, turvallinen asiointi) ja **Digiturva-jäsenyys**
(24,90 € / 39,90 €/kk) – huijausvahti, jossa asiakas lähettää kuvakaappauksen
epäilyttävästä viestistä ja saa vastauksen (tekoäly esiseuloo, ihminen varmistaa).

Tekniikka: pelkkää HTML:ää ja CSS:ää, kevyt vapaaehtoinen JavaScript. **Ei
build-vaihetta eikä riippuvuuksia ajossa** – nopea myös vanhoilla laitteilla.
Ei ulkoisia fontteja eikä seurantaa (tietosuojasyistä).

## Sivut

| Tiedosto | Sisältö |
| --- | --- |
| `index.html` | Etusivu: kotikäynnit, Digiturva-nosto, näin se toimii, palautteet |
| `palvelut.html` | Kotikäyntipalvelut kiinteillä hinnoilla |
| `digiturva.html` | Huijausvahti + animoitu esimerkki + jäsenyystasot + UKK |
| `hinnat.html` | Hinnasto, jäsenyydet ja kotitalousvähennys |
| `vinkit.html` + `vinkit-*.html` | Vinkit-osio: 3 huijausvalistusartikkelia (Google-näkyvyys) |
| `lahjakortti.html` | Lahjakortit (kohderyhmänä aikuiset lapset) |
| `meista.html` | Yritys-esittely, perustajan tarina, tiimi, lupaukset, luotettavuusmerkit |
| `yhteys.html` | Puhelin, soittopyyntölomake (suostumus), WhatsApp |
| `tietosuoja.html` | GDPR-tietosuojaseloste (luonnospohja) |

Aputiedostot: `css/style.css`, `js/main.js` (esiintuloanimaatiot + demo),
`favicon.svg`, `og-kuva.svg`/`og-kuva.png` (jakokuva), `robots.txt`, `sitemap.xml`.

## Sivujen tuottaminen (kehittäjälle)

Ylä- ja alatunniste sekä `<head>` ovat samat joka sivulla. Jotta ne pysyvät
yhtenäisinä, sivut **generoidaan** skriptillä – itse sivusto on silti tavallista
staattista HTML:ää eikä tarvitse skriptiä toimiakseen.

```sh
python3 tools/build.py      # kirjoittaa kaikki *.html-tiedostot uudelleen
```

Muokkaa sisältöä ja paikkamerkkejä tiedostossa `tools/build.py` (ei käsin
yksittäisiä HTML-tiedostoja), aja skripti ja committaa tulos.

## Ennen julkaisua: täytä paikkamerkit (tiedostossa `tools/build.py`)

- [ ] `BRAND` / nimi → **eTuki** on nykyinen työnimi (vaihtoehto: **Digissä**).
      Vaihto: päivitä `BRAND`-vakio, logon teksti (`header`-funktio) ja `og-kuva.svg`,
      ja aja generaattori + OG-kuvan uudelleenrender.
- [ ] `NIMI` → perustajan nimi (myös `meista`-sivun tiimikorteissa `[Nimi]`)
- [ ] `ALUE` → palvelualue ([Kaupunki] ja lähialueet, myös `meista`-tekstissä)
- [ ] **Ennakkoperintärekisteri** – varmista, että yritys on rekisterissä ENNEN kuin
      kotitalousvähennys-väite julkaistaan (`build_hinnat`, `build_meista`)
- [ ] **Vastuuvakuutus** – ota vakuutus ja päivitä `meista`-sivun merkki todeksi
- [ ] **Tiimikortit** (`build_meista`) – täytä oikeat nimet, roolit ja esittelyt
- [ ] `YTUNNUS` → oikea Y-tunnus
- [ ] `PUH_NUM` / `PUH_NAYTTO` / `WA_NUM` → oikea puhelinnumero
- [ ] `EMAIL`, `DOMAIN` → oikea sähköposti ja verkkotunnus (myös `robots.txt`, `sitemap.xml`)
- [ ] Hinnat (kerta 79–149 €, jäsenyydet 24,90 / 39,90 €) – tarkista
- [ ] Soittopyyntölomake (`build_yhteys`): luo lomake **EU-alueen** palveluun ja
      korvaa `formspree.io/f/LOMAKETUNNUS` (ks. tietosuoja alla)
- [ ] Asiakaspalautteet (`build_index`): korvaa esimerkit oikeilla, **asiakkaan
      luvalla** julkaistavilla palautteilla
- [ ] Tietosuojaseloste (`tietosuoja.html`): täytä rekisterinpitäjä ja käsittelijät
- [ ] Kotitalousvähennys: tarkista voimassa olevat luvut **vero.fi**

## Tietosuoja (EU / GDPR)

Sivusto on rakennettu tietosuoja edellä, koska se kerää henkilötietoja
(yhteydenotot) ja Digiturvassa käsitellään asiakkaiden kuvakaappauksia:

- **Ei ulkoisia fontteja** – Google Fonts -CDN poistettu (se siirtäisi kävijän
  IP-osoitteen Googlelle). Käytössä järjestelmäfontit. *Halutessa* voit
  self-hostata Inter-fontin: lataa `woff2`-tiedostot kansioon `fonts/`, lisää
  `@font-face` tiedostoon `css/style.css` ja liitä OFL-lisenssi mukaan.
- **Suostumus** lomakkeessa: pakollinen valintaruutu + linkki tietosuojaselosteeseen.
- **Tietojen minimointi**: lomake kerää vain nimen ja puhelinnumeron.
- **Lomakepalvelu**: oletuksena Formspree (US) on vain paikkamerkki. Suosi
  EU-/ETA-alueella toimivaa lomake- ja laskutuspalvelua, tai kuvaa siirto
  selosteessa.
- **Kuvakaappaukset**: käsitellään luottamuksellisesti, vain arviointia varten,
  poistetaan käsittelyn jälkeen; pankkitunnuksia ei koskaan pyydetä.

## Tiekartta: oikea "turva-tekoäly" ja maksut (ei vielä toteutettu)

Staattinen sivu ei voi ajaa tekoälyä turvallisesti (API-avain paljastuisi). Nyt
huijaustarkistus toimii ihmisvetoisesti WhatsAppin kautta. Automatisointi vaatii
pienen taustapalvelun:

- **Serverless-funktio** (esim. Cloudflare Workers / Vercel, mieluiten EU-alue),
  joka kutsuu kuva-analyysiin kykenevää mallia; avain pysyy palvelimella.
- **Maksut**: Stripe tai kotimainen vaihtoehto jäsenmaksuihin (toistuvaislaskutus).
- **GDPR-by-design**: EU-sijainti, käsittelysopimus (DPA) tekoälypalvelun kanssa,
  tietojen minimointi, kuvien automaattinen poisto, käsittelytoimien seloste (ROPA),
  ei koskaan tunnusten tallennusta.

## Julkaisu GitHub Pagesissa

1. **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   valitse haara `claude/stoic-curie-npiqk8` ja kansio `/ (root)` → **Save**.
2. Sivusto: `https://hamzamao.github.io/et-kotisivu/` (n. minuutin kuluttua).
3. Oma verkkotunnus: lisää Pagesin asetuksiin ja tee nimipalvelutietueet.

`.nojekyll` on mukana, joten GitHub tarjoaa tiedostot sellaisenaan.

## Paikallinen esikatselu

```sh
python3 -m http.server 8000     # avaa http://localhost:8000
```
