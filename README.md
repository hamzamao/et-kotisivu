# ET Digiapu – kotisivut

Staattinen kotisivusto digiapupalvelulle: kotikäyntejä senioreille puhelimen,
netin, television ja turvallisen asioinnin kanssa. Ei buildia, ei riippuvuuksia
– pelkkää HTML:ää ja CSS:ää, jotta sivut latautuvat nopeasti myös vanhoilla
laitteilla ja niitä on helppo päivittää.

## Sivut

| Tiedosto           | Sisältö                                              |
| ------------------ | ---------------------------------------------------- |
| `index.html`       | Etusivu: mitä, missä, iso puhelinnumero               |
| `palvelut.html`    | Palvelut kiinteillä hinnoilla                         |
| `hinnat.html`      | Hinnasto + kotitalousvähennys                         |
| `minusta.html`     | Esittely, kasvokuva, lupaukset asiakkaalle            |
| `lahjakortti.html` | Lahjakortit (kohderyhmänä aikuiset lapset)            |
| `yhteys.html`      | Puhelin, soittopyyntölomake, palvelualue              |

Huom: ylä- ja alatunniste on kopioitu jokaiselle sivulle, koska sivustolla ei
ole build-vaihetta. Jos muutat valikkoa tai alatunnistetta, muuta se kaikkiin
kuuteen tiedostoon.

## Ennen julkaisua: täytä paikkamerkit

Etsi ja korvaa kaikista `.html`-tiedostoista:

- [ ] **`Etunimi Sukunimi`** → oma nimesi
- [ ] **`[Kaupunki]`** → palvelualueesi kaupunki
- [ ] **`[0000000-0]`** → oikea Y-tunnus
- [ ] **`040 123 4567`** ja **`+358401234567`** → oikea puhelinnumero
      (näkyvä teksti JA `tel:`-linkit, myös `index.html`:n JSON-LD-lohko)
- [ ] **`info@etdigiapu.fi`** ja **`https://www.etdigiapu.fi/`** → oikea
      sähköposti ja verkkotunnus
- [ ] **Hinnat** – tarkista, että 79–149 € hinnat vastaavat omaa hinnoitteluasi
- [ ] **`img/kasvokuva.svg`** → oikea kasvokuva (`minusta.html`)
- [ ] **Soittopyyntölomake** (`yhteys.html`) – luo ilmainen lomake osoitteessa
      [formspree.io](https://formspree.io) ja vaihda `LOMAKETUNNUS` saamaasi
      tunnukseen
- [ ] **Kotitalousvähennys** (`hinnat.html`) – tarkista ajantasaiset summat ja
      prosentti osoitteesta [vero.fi](https://www.vero.fi)

## Julkaisu GitHub Pagesissa

1. GitHubissa: **Settings → Pages → Source: Deploy from a branch**, valitse
   haluamasi haara ja kansioksi `/ (root)`.
2. Sivusto on hetken päästä osoitteessa `https://<käyttäjä>.github.io/et-kotisivu/`.
3. Oma verkkotunnus (esim. `etdigiapu.fi`): osta tunnus, lisää se Pagesin
   asetuksiin ja tee nimipalveluun ohjeiden mukaiset CNAME-/A-tietueet.

## Paikallinen esikatselu

Avaa `index.html` suoraan selaimessa, tai käynnistä kevyt palvelin:

```sh
python3 -m http.server 8000
```

ja avaa <http://localhost:8000>.
