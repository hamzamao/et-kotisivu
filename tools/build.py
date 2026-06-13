#!/usr/bin/env python3
"""Generaattori, joka tuottaa sivuston staattiset HTML-tiedostot.

Tämä on KEHITYSTYÖKALU: aja kerran ja committaa tuotetut .html-tiedostot.
Itse sivusto on tavallista staattista HTML:ää eikä tarvitse tätä toimiakseen.
Ajo:  python3 tools/build.py
"""
import os
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Paikkamerkit (vaihda oikeiksi ennen julkaisua) ---
DOMAIN = "https://www.etdigiapu.fi"
PUH_NUM = "+358401234567"
PUH_NAYTTO = "040&nbsp;123&nbsp;4567"
PUH_NAYTTO_TAVALLINEN = "040 123 4567"
WA_NUM = "358401234567"
WA_VIESTI = "Hei, haluaisin tarkistuttaa epäilyttävän viestin."
WA_URL = "https://wa.me/%s?text=%s" % (WA_NUM, urllib.parse.quote(WA_VIESTI))
EMAIL = "info@etdigiapu.fi"
YTUNNUS = "[0000000-0]"
NIMI = "Etunimi Sukunimi"
ALUE = "[Kaupunki] ja lähialueet"

# --- SVG-ikonit (viivapiirros, perii värin currentColor) ---
def _svg(body):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true">%s</svg>') % body

I = {
    "puhelin": _svg('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>'),
    "wifi": _svg('<path d="M5 13a10 10 0 0 1 14 0"/><path d="M8.5 16.5a5 5 0 0 1 7 0"/><line x1="12" y1="20" x2="12.01" y2="20"/><path d="M2 9a15 15 0 0 1 20 0"/>'),
    "tv": _svg('<rect x="2" y="7" width="20" height="13" rx="2"/><polyline points="8 3 12 7 16 3"/>'),
    "kilpi": _svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>'),
    "posti": _svg('<rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3 7 12 13 21 7"/>'),
    "verkko": _svg('<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/>'),
    "tulostin": _svg('<polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>'),
    "palapeli": _svg('<path d="M9 3a2 2 0 0 1 4 0c0 .5 0 1 .5 1H16a1 1 0 0 1 1 1v2.5c0 .5.5.5 1 .5a2 2 0 0 1 0 4c-.5 0-1 0-1 .5V19a1 1 0 0 1-1 1h-3a1 1 0 0 1-1-1c0-.5-.5-1-1-1a2 2 0 0 0 0 4"/>'),
    "sydan": _svg('<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/>'),
    "lukko": _svg('<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>'),
    "esto": _svg('<circle cx="12" cy="12" r="10"/><line x1="4.9" y1="4.9" x2="19.1" y2="19.1"/>'),
    "puhe": _svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
    "varoitus": _svg('<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'),
    "kuva": _svg('<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/>'),
    "wa": _svg('<path d="M21 11.5a8.4 8.4 0 0 1-12.3 7.4L3 21l2.2-5.6A8.4 8.4 0 1 1 21 11.5z"/>'),
}

LOGO_SVG = ('<svg viewBox="0 0 64 64" aria-hidden="true">'
            '<rect width="64" height="64" rx="14" fill="#0b1d3a"/>'
            '<path d="M32 11l16 6v12c0 11-7 18-16 23-9-5-16-12-16-23V17l16-6z" fill="#1d4ed8"/>'
            '<path d="M23 33l6 6 12-13" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="49" cy="17" r="6" fill="#ea580c"/></svg>')

# Heron pieni kuvitus (laite + kilpi)
HERO_SVG = ('<svg viewBox="0 0 320 320" role="img" aria-label="Puhelin ja suojakilpi">'
            '<rect x="92" y="40" width="136" height="240" rx="24" fill="#0e203f" stroke="#2a4a82" stroke-width="3"/>'
            '<rect x="104" y="64" width="112" height="180" rx="10" fill="#14315f"/>'
            '<circle cx="160" cy="262" r="9" fill="#2a4a82"/>'
            '<g><circle cx="160" cy="150" r="64" fill="#1d4ed8"/>'
            '<path d="M160 116l30 11v22c0 20-13 33-30 41-17-8-30-21-30-41v-22l30-11z" fill="#0b1d3a"/>'
            '<path d="M146 150l9 9 19-20" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>'
            '<circle cx="214" cy="92" r="16" fill="#ea580c"/>'
            '<path d="M209 92l4 4 7-8" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')

NAV = [
    ("index.html", "Etusivu"),
    ("palvelut.html", "Palvelut"),
    ("digiturva.html", "Digiturva"),
    ("hinnat.html", "Hinnat"),
    ("vinkit.html", "Vinkit"),
    ("lahjakortti.html", "Lahjakortti"),
    ("yhteys.html", "Yhteystiedot"),
]


def header(active):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items += '<li><a href="%s"%s>%s</a></li>' % (href, cur, label)
    return (
        '<a class="ohita" href="#sisalto">Siirry sisältöön</a>'
        '<header class="ylatunniste"><div class="sisalto">'
        '<a class="logo" href="index.html">%s ET<span style="color:#ea580c">.</span> Digiapu</a>'
        '<nav class="navigaatio" aria-label="Päävalikko"><ul>%s</ul></nav>'
        '</div></header>' % (LOGO_SVG, items)
    )


FOOTER = (
    '<footer class="alatunniste"><div class="sisalto">'
    '<div class="sarakkeet">'
    '<div><h3>ET Digiapu &amp; Digiturva</h3>'
    '<p>Digiapua kotiin ja suojaa huijauksia vastaan – ihmiseltä, jota et joudu jonottamaan.</p>'
    '<p>%s · Y-tunnus %s</p></div>'
    '<div><h3>Yhteystiedot</h3>'
    '<p>Puhelin: <a href="tel:%s">%s</a></p>'
    '<p>WhatsApp: <a href="%s">%s</a></p>'
    '<p>Sähköposti: <a href="mailto:%s">%s</a></p>'
    '<p>Palvelualue: %s</p></div>'
    '<div><h3>Sivut</h3><ul>'
    '<li><a href="palvelut.html">Palvelut</a></li>'
    '<li><a href="digiturva.html">Digiturva-jäsenyys</a></li>'
    '<li><a href="hinnat.html">Hinnat ja kotitalousvähennys</a></li>'
    '<li><a href="vinkit.html">Vinkit ja artikkelit</a></li>'
    '<li><a href="lahjakortti.html">Lahjakortti</a></li>'
    '<li><a href="minusta.html">Minusta</a></li>'
    '<li><a href="tietosuoja.html">Tietosuojaseloste</a></li>'
    '</ul></div></div>'
    '<p class="pohja">En koskaan kysy tai käsittele pankkitunnuksiasi tai korttisi tietoja – missään tilanteessa.</p>'
    '</div></footer>'
) % (NIMI, YTUNNUS, PUH_NUM, PUH_NAYTTO_TAVALLINEN, WA_URL, PUH_NAYTTO_TAVALLINEN, EMAIL, EMAIL, ALUE)

SOITA_PALKKI = ('<div class="soita-palkki"><a href="tel:%s" class="nappi">%s Soita %s</a></div>'
                % (PUH_NUM, I["puhelin"], PUH_NAYTTO_TAVALLINEN))


def page(slug, title, desc, body, active=None, extra_jsonld="", scripts=True):
    active = active or slug
    canonical = "%s/%s" % (DOMAIN, "" if slug == "index.html" else slug)
    og_img = "%s/og-kuva.png" % DOMAIN
    head = (
        '<!DOCTYPE html><html lang="fi"><head>'
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>%s</title>'
        '<meta name="description" content="%s">'
        '<link rel="canonical" href="%s">'
        '<link rel="icon" href="favicon.svg" type="image/svg+xml">'
        '<meta property="og:type" content="website">'
        '<meta property="og:locale" content="fi_FI">'
        '<meta property="og:site_name" content="ET Digiapu &amp; Digiturva">'
        '<meta property="og:title" content="%s">'
        '<meta property="og:description" content="%s">'
        '<meta property="og:image" content="%s">'
        '<meta property="og:url" content="%s">'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%s">'
        '<meta name="twitter:description" content="%s">'
        '<meta name="twitter:image" content="%s">'
        '<link rel="stylesheet" href="css/style.css">'
        '<script>document.documentElement.className+=" js";</script>'
        '%s</head><body>'
    ) % (title, desc, canonical, title, desc, og_img, canonical,
         title, desc, og_img, extra_jsonld)
    tail = SOITA_PALKKI + (('<script src="js/main.js" defer></script>') if scripts else "") + '</body></html>'
    return head + header(active) + '<main id="sisalto">' + body + '</main>' + FOOTER + tail


def write(slug, html):
    with open(os.path.join(ROOT, slug), "w", encoding="utf-8") as f:
        f.write(html)


# ----------------------------------------------------------------------------
# Sivujen sisällöt
# ----------------------------------------------------------------------------

def hero():
    return (
        '<section class="hero"><div class="sisalto">'
        '<div><span class="kulmake">Digiapua ja digiturvaa · %s</span>'
        '<h1>Laitteet kuntoon kotonasi – ja suoja huijauksia vastaan</h1>'
        '<p class="alaotsikko">Autan puhelimen, netin ja television kanssa kiireettä ja '
        'selkokielellä. Digiturva-jäsenenä saat lisäksi oman huijausvahdin: lähetä kuva '
        'epäilyttävästä viestistä, ja saat vastauksen minuuteissa.</p>'
        '<div class="hero-cta">'
        '<a class="nappi" href="tel:%s">%s Soita %s</a>'
        '<a class="nappi laidalla" href="digiturva.html">Tutustu Digiturvaan</a></div>'
        '<ul class="merkit"><li>✓ Kiinteät hinnat</li><li>✓ Kotitalousvähennys</li>'
        '<li>✓ Sama tuttu auttaja</li><li>✓ Ei jonoja, ei botteja</li></ul></div>'
        '<div class="hero-kuva">%s</div>'
        '</div></section>'
    ) % (ALUE, PUH_NUM, I["puhelin"], PUH_NAYTTO_TAVALLINEN, HERO_SVG)


def kortti(ikoni, otsikko, teksti, hinta=None):
    h = ('<span class="hinta">%s</span>' % hinta) if hinta else ""
    return ('<li class="kortti"><div class="ikoni">%s</div><h3>%s</h3>'
            '<p class="haalea">%s</p>%s</li>') % (I[ikoni], otsikko, teksti, h)


def sivuotsikko(kulmake, otsikko, teksti):
    return ('<section class="sivuotsikko"><div class="sisalto">'
            '<span class="kulmake">%s</span><h1>%s</h1><p>%s</p></div></section>'
            ) % (kulmake, otsikko, teksti)


# --- index ---
def build_index():
    kortit = (kortti("posti", "Uusi puhelin käyttökuntoon",
                     "Siirrän kuvat, yhteystiedot ja WhatsApp-viestit vanhasta puhelimesta uuteen – mitään ei katoa.", "89 €")
              + kortti("wifi", "Netti ja reititin kuntoon",
                       "Kytken kuituliittymän ja reitittimen ja varmistan, että netti toimii joka huoneessa.", "89 €")
              + kortti("tv", "TV-boksi ja älytelevisio",
                       "Asennan TV-boksin tai uuden television ja opastan kaukosäätimen ja suoratoistopalvelut.", "89 €")
              + kortti("kilpi", "Turvakäynti",
                       "Laitan tietoturvan kuntoon ja opastan, miten huijaukset tunnistaa. <strong>En koskaan kysy pankkitunnuksiasi.</strong>", "99 €"))
    palautteet = (
        '<section class="osio"><div class="sisalto reveal">'
        '<div class="osio-otsikko"><span class="ylarivi">Asiakkaiden ääni</span>'
        '<h2>Mitä asiakkaat sanovat</h2></div>'
        '<div class="huomio varoitus"><p><strong>Huom:</strong> alla on esimerkkimuotoilu. '
        'Oikeat, asiakkaiden luvalla julkaistavat palautteet lisätään tähän myöhemmin.</p></div>'
        '<div class="palautteet">'
        '<div class="palaute"><div class="tahdet" aria-label="5 / 5 tähteä">★★★★★</div>'
        '<blockquote>[Asiakaspalaute lisätään – esim. kokemus puhelimen vaihdosta.]</blockquote>'
        '<p class="nimi">[Nimi, paikkakunta]</p></div>'
        '<div class="palaute"><div class="tahdet" aria-label="5 / 5 tähteä">★★★★★</div>'
        '<blockquote>[Asiakaspalaute lisätään – esim. lapsi osti käynnin vanhemmalleen.]</blockquote>'
        '<p class="nimi">[Nimi, paikkakunta]</p></div>'
        '<div class="palaute"><div class="tahdet" aria-label="5 / 5 tähteä">★★★★★</div>'
        '<blockquote>[Asiakaspalaute lisätään – esim. Digiturva esti huijauksen.]</blockquote>'
        '<p class="nimi">[Nimi, paikkakunta]</p></div>'
        '</div></div></section>'
    )
    body = (
        hero()
        + '<section class="osio"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Kotikäynnit</span>'
          '<h2>Missä voin auttaa?</h2><p class="haalea">Tulen kotiisi, laitan laitteet '
          'kuntoon ja opastan käytön niin monta kertaa kuin tarvitaan.</p></div>'
          '<ul class="korttilista">' + kortit + '</ul>'
          '<p><a class="nappi toissijainen" href="palvelut.html">Kaikki palvelut ja hinnat</a></p>'
          '</div></section>'
        + '<section><div class="sisalto"><div class="kaista reveal">'
          '<span class="kulmake">Uutta · ET Digiturva</span>'
          '<h2>Epäilyttävä viesti? Älä arvaa – tarkistuta se.</h2>'
          '<p>Digiturva-jäsenenä lähetät kuvakaappauksen epäilyttävästä viestistä WhatsAppilla. '
          'Tekoäly analysoi sen heti, minä varmistan tuloksen, ja saat selkeän vastauksen: '
          '<strong>huijaus vai ei – ja mitä tehdä seuraavaksi.</strong></p>'
          '<p>Jäsenyys alkaen 24,90 €/kk, ei sitoutumisaikaa.</p>'
          '<a class="nappi" href="digiturva.html">Lue lisää Digiturvasta</a></div></div></section>'
        + '<section class="osio"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Helppoa alusta loppuun</span>'
          '<h2>Näin se toimii</h2></div><ol class="vaiheet">'
          '<li><h3>Soita tai jätä soittopyyntö</h3><p>Kerro omin sanoin, mikä laite kiusaa. '
          'Ei tarvitse osata termejä – sitä varten minä olen.</p></li>'
          '<li><h3>Tulen kotiisi sovittuna aikana</h3><p>Laitan laitteet kuntoon ja opastan '
          'käytön rauhassa. Kerron hinnan aina etukäteen.</p></li>'
          '<li><h3>Apu ei lopu käyntiin</h3><p>Jos jokin unohtuu, voit soittaa. '
          'Digiturva-jäsenenä saat tuen ja huijausvahdin jatkuvasti.</p></li></ol></div></section>'
        + palautteet
        + '<section class="osio"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Miksi minä?</span>'
          '<h2>Ihminen, joka oikeasti välittää</h2></div>'
          '<p>Moni ikäihminen jää laitteidensa kanssa yksin – omilla lapsilla ei aina ole aikaa '
          'tai kärsivällisyyttä. Minulla on. Kuuden vuoden asiakastyökokemus on opettanut '
          'selittämään asiat ilman tietokonekieltä, ja autan sinua samalla tavalla kuin auttaisin '
          'omia vanhempiani. <a href="minusta.html">Lue lisää minusta.</a></p>'
          '<div class="huomio"><p><strong>Tiesitkö?</strong> Kotona tehty tietotekniikan asennus- '
          'ja opastustyö oikeuttaa <a href="hinnat.html">kotitalousvähennykseen</a>. Saat aina '
          'kuitin, jossa työn osuus on eritelty valmiiksi verottajaa varten.</p></div>'
          '</div></section>'
    )
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org",'
              '"@type":"LocalBusiness","name":"ET Digiapu & Digiturva",'
              '"description":"Digiapua kotiin senioreille sekä Digiturva-jäsenyys: huijaustarkistus, etätuki ja turvallinen asiointi.",'
              '"telephone":"%s","email":"%s","areaServed":"%s","priceRange":"€€","url":"%s/"}</script>'
              ) % (PUH_NUM, EMAIL, ALUE, DOMAIN)
    write("index.html", page("index.html",
        "ET Digiapu & Digiturva – digiapua kotiin ja suoja huijauksia vastaan",
        "Digiapua kotiisi: puhelin, netti ja TV kuntoon kiinteällä hinnalla. Digiturva-jäsenyys suojaa huijauksilta – lähetä kuvakaappaus epäilyttävästä viestistä ja saat vastauksen minuuteissa.",
        body, extra_jsonld=jsonld))


# --- palvelut ---
def build_palvelut():
    kortit = (
        kortti("posti", "Puhelimen vaihto ja tietojen siirto",
               "Otan uuden puhelimen käyttöön ja siirrän kuvat, yhteystiedot ja WhatsApp-viestit vanhasta. Opastan tärkeimmät toiminnot ja kirjoitan tunnukset talteen sinulle.", "89 €")
        + kortti("wifi", "Kuituliittymä ja reititin käyttökuntoon",
                 "Kytken reitittimen, yhdistän laitteesi verkkoon ja varmistan, että netti kuuluu koko kotiin. Vaihdan myös turvalliset salasanat.", "89 €")
        + kortti("tv", "TV-boksi tai älytelevisio asennettuna",
                 "Asennan TV-boksin tai uuden television, viritän kanavat ja otan halutessasi käyttöön suoratoistopalvelut (esim. Yle Areena). Opastan kaukosäätimen rauhassa.", "89 €")
        + kortti("tulostin", "Tulostin, sähköposti ja salasanat kuntoon",
                 "Asennan tulostimen, laitan sähköpostin toimimaan kaikilla laitteillasi ja kokoan salasanat turvalliseen järjestykseen.", "79 €")
        + kortti("kilpi", "Turvakäynti – suojaudu huijauksilta",
                 "Käymme yhdessä läpi, miten huijaukset tunnistaa, ja laitan laitteittesi tietoturvan kuntoon. Opastan turvallisen pankki- ja viranomaisasioinnin (esim. OmaKanta, Kela).", "99 €")
        + kortti("palapeli", "Muu apu tuntityönä",
                 "Mikä tahansa muu laite- tai digipulma: läppärit, tabletit, valokuvien siirto, videopuhelut lastenlasten kanssa…", "79 € <small>/ tunti</small>")
    )
    body = (
        sivuotsikko("Kotikäynnit", "Palvelut",
                    "Kaikki tehdään kotonasi, kiireettä ja selkokielellä. Hinnat ovat kiinteitä, joten tiedät kustannuksen etukäteen – ei yllätyksiä.")
        + '<section class="osio"><div class="sisalto reveal"><ul class="korttilista">'
        + kortit + '</ul>'
        + '<div class="huomio turva"><p><strong>Turvalupaukseni:</strong> en koskaan kysy tai '
          'käsittele pankkitunnuksiasi tai maksukorttisi tietoja. Kaikki asiointi tehdään niin, '
          'että tunnukset pysyvät vain sinun käsissäsi.</p></div></div></section>'
        + '<section><div class="sisalto"><div class="kaista reveal">'
          '<span class="kulmake">Jatkuva apu</span>'
          '<h2>Haluatko tuen, joka ei lopu yhteen käyntiin?</h2>'
          '<p>Digiturva-jäsenenä saat oman huijausvahdin, puhelintuen ja tarvittaessa kotikäynnit '
          '– kuukausihintaan, ilman sitoutumisaikaa.</p>'
          '<a class="nappi" href="digiturva.html">Tutustu Digiturvaan</a></div></div></section>'
    )
    write("palvelut.html", page("palvelut.html",
        "Palvelut – ET Digiapu | Digiapua kotiin",
        "Puhelimen vaihto ja tietojen siirto, reitittimen asennus, TV-boksin asennus, tulostin ja sähköposti kuntoon sekä turvakäynti huijauksia vastaan. Kiinteät hinnat, kotitalousvähennys.",
        body))


# --- digiturva ---
def build_digiturva():
    demo = (
        '<div class="demo" aria-label="Esimerkki huijaustarkistuksesta">'
        '<div class="demo-otsake"><span class="pallura"></span> ET Digiturva · huijausvahti</div>'
        '<div class="kupla asiakas"><span class="liite">%s Kuvakaappaus.png</span></div>'
        '<div class="kupla asiakas">Tuliko tämä oikeasti Postilta? Pitää muka maksaa 2,99 € tullimaksu.</div>'
        '<div class="kupla turva"><span class="lippu">%s Tämä on huijaus</span>'
        'Tunnusmerkit: linkki vie osoitteeseen <strong>posti-fi.xyz</strong> (ei posti.fi), '
        'viesti kiirehtii maksamaan ja pyytää korttitietoja.</div>'
        '<div class="kupla turva">Älä klikkaa linkkiä äläkä anna korttitietoja. Poista viesti. '
        'Jos ehdit jo klikata, soita minulle – autan heti.</div>'
        '<p class="demo-vihje">Esimerkki – näin huijausvahti vastaa.</p>'
        '</div>'
    ) % (I["kuva"], I["varoitus"])

    kortit = (
        kortti("puhe", "Tekstiviestit", '"Pakettisi odottaa", "tilisi suljetaan", väärennetyt linkit. Tunnistan huijaustekstit ja vaaralliset linkit.')
        + kortti("posti", "Sähköpostit", "Väärennetyt viestit pankilta, Postilta tai Verolta. Tarkistan lähettäjän ja sisällön puolestasi.")
        + kortti("verkko", "Verkkosivut ja mainokset", 'Epäilyttävät kaupat ja "olet voittanut" -sivut. Kerron, onko sivu turvallinen vai huijaus.')
        + kortti("esto", "Puhelut ja ”tukihenkilöt”", "Soittaja, joka pyytää tunnuksia tai etäyhteyttä. Neuvon, milloin pitää sulkea puhelin heti.")
    )
    body = (
        sivuotsikko("ET Digiturva", "Oma huijausvahti taskussasi",
                    "Huijaukset näyttävät nykyään aidoilta. Et ole yksin niiden kanssa: epäilyttävän viestin voi aina tarkistuttaa – ja vastauksen antaa ihminen, ei pelkkä kone.")
        + '<section class="osio"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Miten se toimii</span>'
          '<h2>Epäilyttävä viesti? Lähetä kuva – saat vastauksen minuuteissa.</h2>'
          '<p class="haalea">Tekstiviesti paketista, kummallinen sähköposti pankilta, outo '
          'verkkosivu tai soitto, joka pyytää tunnuksia – tarkistuta se ennen kuin teet mitään.</p></div>'
          + demo +
          '<ol class="vaiheet">'
          '<li><h3>Ota kuvakaappaus</h3><p>Ota kuva epäilyttävästä viestistä. Opastan kuvan '
          'ottamisen, jos se tuntuu hankalalta.</p></li>'
          '<li><h3>Lähetä se minulle</h3><p>Lähetä kuva WhatsAppilla tai tekstiviestillä '
          'Digiturva-numeroon. Yksi viesti riittää.</p></li>'
          '<li><h3>Tekoäly analysoi heti</h3><p>Turva-tekoäly tunnistaa tyypilliset huijauksen '
          'merkit sekunneissa ja merkitsee, mikä viestissä on epäilyttävää.</p></li>'
          '<li><h3>Ihminen varmistaa ja vastaa</h3><p>Tarkistan tuloksen itse ja vastaan '
          'selkokielellä: <strong>huijaus vai ei – ja mitä tehdä seuraavaksi.</strong></p></li></ol>'
          '<div class="huomio turva"><p><strong>Ihminen ratkaisee, ei botti.</strong> Tekoäly '
          'auttaa tunnistamaan huijaukset nopeasti, mutta lopullisen arvion teen aina minä. Et '
          'koskaan jää pelkän koneen vastauksen varaan – etkä joudu jonottamaan.</p></div>'
          '</div></section>'
        + '<section class="osio"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Mitä Digiturva tarkistaa</span>'
          '<h2>Suoja kaikkiin yleisimpiin huijauksiin</h2></div>'
          '<ul class="korttilista">' + kortit + '</ul></div></section>'
        + '<section class="osio" id="hinnat"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Jäsenyys</span>'
          '<h2>Valitse oma turvataso</h2><p class="haalea">Ei sitoutumisaikaa – voit lopettaa '
          'milloin tahansa. Jäsenyyden voi maksaa myös läheinen lahjaksi.</p></div>'
          '<div class="paketit">'
          '<div class="paketti"><h3>Digiturva Perus</h3>'
          '<p class="kk-hinta">24,90 € <small>/ kk</small></p><ul>'
          '<li>Huijausvahti: lähetä kuva, vastaus minuuteissa (arkisin)</li>'
          '<li>Puhelintuki lyhyisiin digipulmiin</li>'
          '<li>Muistutukset tärkeistä päivityksistä ja tietoturvasta</li>'
          '<li>Ei sitoutumisaikaa</li></ul>'
          '<a class="nappi toissijainen" href="yhteys.html">Liity jäseneksi</a></div>'
          '<div class="paketti suosituin"><span class="leima">Suosituin</span>'
          '<h3>Digiturva Plus</h3><p class="kk-hinta">39,90 € <small>/ kk</small></p><ul>'
          '<li>Kaikki Perus-tason edut</li>'
          '<li>Huijausvahti myös iltaisin ja viikonloppuisin</li>'
          '<li>Yksi kotikäynti puolen vuoden välein sisältyy</li>'
          '<li>Etätuki ruudunjaolla – et joudu odottamaan käyntiä</li>'
          '<li>Omaisraportti: läheinen saa halutessaan tiedon, että kaikki on kunnossa</li></ul>'
          '<a class="nappi" href="yhteys.html">Liity jäseneksi</a></div></div>'
          '<div class="huomio"><p>Plus-jäsenyyteen sisältyvä kotikäynti on '
          '<a href="hinnat.html">kotitalousvähennyskelpoista</a> työtä. Saat kuitin, jossa työn '
          'osuus on eritelty valmiiksi.</p></div></div></section>'
        + '<section class="osio faq"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Usein kysytyt</span>'
          '<h2>Kysymyksiä Digiturvasta</h2></div>'
          '<details><summary>Mihin numeroon lähetän epäilyttävän viestin kuvan?</summary>'
          '<p>Saat jäsenenä oman Digiturva-numeron, johon lähetät kuvan WhatsAppilla tai '
          'tekstiviestillä. Opastan kuvan ottamisen ja lähettämisen ensimmäisellä kerralla.</p></details>'
          '<details><summary>Korvaako tämä pankin tai poliisin?</summary>'
          '<p>Ei korvaa. Autan tunnistamaan huijauksen ja kerron, mitä tehdä – esimerkiksi soittaa '
          'pankin omaan asiakaspalveluun tai tehdä rikosilmoitus. Toimin tukenasi, en viranomaisena.</p></details>'
          '<details><summary>Käsitelläänkö lähettämiäni kuvia turvallisesti?</summary>'
          '<p>Kyllä. Kuvat käsitellään luottamuksellisesti ja vain tarkistusta varten, ja ne '
          'poistetaan käsittelyn jälkeen. <strong>En koskaan pyydä pankkitunnuksiasi.</strong> '
          'Lue lisää <a href="tietosuoja.html">tietosuojaselosteesta</a>.</p></details>'
          '<details><summary>Voinko lopettaa jäsenyyden milloin vain?</summary>'
          '<p>Voit. Jäsenyydessä ei ole sitoutumisaikaa, ja sen voi lopettaa yhdellä soitolla tai viestillä.</p></details>'
          '</div></section>'
        + '<section><div class="sisalto"><div class="kaista reveal">'
          '<h2>Aloita turva jo tänään</h2>'
          '<p>Soita, niin käymme yhdessä läpi sopivan jäsenyyden ja otan huijausvahdin käyttöösi heti.</p>'
          '<a class="nappi" href="tel:%s">%s Soita %s</a></div></div></section>'
          % (PUH_NUM, I["puhelin"], PUH_NAYTTO_TAVALLINEN)
    )
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Service",'
              '"serviceType":"Huijaustarkistus ja digiturvan jäsenyys",'
              '"provider":{"@type":"LocalBusiness","name":"ET Digiapu & Digiturva"},'
              '"areaServed":"Suomi","offers":[{"@type":"Offer","name":"Digiturva Perus","price":"24.90","priceCurrency":"EUR"},'
              '{"@type":"Offer","name":"Digiturva Plus","price":"39.90","priceCurrency":"EUR"}]}</script>')
    write("digiturva.html", page("digiturva.html",
        "Digiturva – huijausvahti ja jäsenyys senioreille | ET Digiapu",
        "ET Digiturva on jatkuva suoja huijauksia vastaan: lähetä kuvakaappaus epäilyttävästä viestistä, tekoäly analysoi sen ja ihminen varmistaa. Jäsenyys alkaen 24,90 €/kk, ei sitoutumisaikaa.",
        body, extra_jsonld=jsonld))


# --- hinnat ---
def build_hinnat():
    body = (
        sivuotsikko("Selkeät hinnat", "Hinnat",
                    "Kiinteät hinnat sisältävät matkat palvelualueella. Maksu käynnin päätteeksi kortilla, MobilePaylla tai laskulla – niin kuin sinulle sopii.")
        + '<section class="osio"><div class="sisalto reveal"><h2>Kotikäynnit</h2>'
          '<table><caption class="nakymaton">Palveluiden hinnasto</caption>'
          '<thead><tr><th scope="col">Palvelu</th><th scope="col">Hinta</th></tr></thead><tbody>'
          '<tr><td>Puhelimen vaihto ja tietojen siirto</td><td>89 €</td></tr>'
          '<tr><td>Kuituliittymä ja reititin käyttökuntoon</td><td>89 €</td></tr>'
          '<tr><td>TV-boksi tai älytelevisio asennettuna</td><td>89 €</td></tr>'
          '<tr><td>Tulostin, sähköposti ja salasanat kuntoon</td><td>79 €</td></tr>'
          '<tr><td>Turvakäynti – suojaudu huijauksilta</td><td>99 €</td></tr>'
          '<tr><td>Muu apu tuntityönä</td><td>79 € / tunti</td></tr>'
          '<tr><td>Jatkoaika samalla käynnillä</td><td>15 € / alkava 15 min</td></tr></tbody></table>'
          '<h2>Digiturva-jäsenyys</h2><p>Jatkuva suoja huijauksia vastaan ja oma tuki '
          'kuukausihintaan, ilman sitoutumisaikaa. <a href="digiturva.html">Lue tarkemmin '
          'Digiturvasta.</a></p>'
          '<table><caption class="nakymaton">Digiturva-jäsenyyden hinnasto</caption>'
          '<thead><tr><th scope="col">Jäsenyys</th><th scope="col">Hinta</th></tr></thead><tbody>'
          '<tr><td>Digiturva Perus – huijausvahti ja puhelintuki</td><td>24,90 € / kk</td></tr>'
          '<tr><td>Digiturva Plus – sis. kotikäynnin ja etätuen</td><td>39,90 € / kk</td></tr>'
          '</tbody></table></div></section>'
        + '<section class="osio"><div class="sisalto reveal">'
          '<div class="osio-otsikko"><span class="ylarivi">Veroetu</span>'
          '<h2>Kotitalousvähennys – saat osan rahoista takaisin</h2></div>'
          '<p>Kotona tehty tietotekniikan asennus- ja opastustyö on <strong>kotitalousvähennykseen '
          'oikeuttavaa työtä</strong>. Vuonna 2025 vähennys on <strong>35 % työn osuudesta</strong>, '
          'enimmäismäärä <strong>1 600 € henkilöä kohden</strong> ja omavastuu <strong>150 € '
          'vuodessa</strong>.</p>'
          '<div class="huomio varoitus"><p><strong>Tulossa mahdollisesti 2026:</strong> hallitus '
          'on esittänyt vähennyksen korottamista 40 %:iin ja enimmäismäärän nostoa 2 100 euroon. '
          'Muutos ei ole vielä vahvistettu – tarkista voimassa olevat tiedot aina osoitteesta '
          '<a href="https://www.vero.fi/henkiloasiakkaat/verokortti-ja-veroilmoitus/tulot-ja-vahennykset/kotitalousvahennys/">vero.fi</a>.</p></div>'
          '<p>Koska omavastuu on 150 € vuodessa, vähennys hyödyttää eniten silloin, kun työ on '
          'isompi tai käyntejä on vuoden aikana useita. Yksittäisestä pienestä käynnistä '
          'vähennystä ei käytännössä jää. Saat minulta aina kuitin, jossa <strong>työn osuus on '
          'eritelty valmiiksi</strong> – ja jos haluat, autan vähennyksen ilmoittamisessa '
          'OmaVerossa.</p>'
          '<div class="huomio"><p><strong>Ei piilokuluja:</strong> kerron aina hinnan ennen työn '
          'aloittamista. Jos en pysty auttamaan pulmassasi, käynti ei maksa mitään.</p></div>'
          '<p><a class="nappi" href="yhteys.html">Soita ja sovi käynti</a></p></div></section>'
    )
    write("hinnat.html", page("hinnat.html",
        "Hinnat ja kotitalousvähennys – ET Digiapu",
        "Selkeät kiinteät hinnat digiavulle kotiin sekä Digiturva-jäsenyys alkaen 24,90 €/kk. Työ oikeuttaa kotitalousvähennykseen (2025: 35 %, enintään 1 600 €).",
        body))


# --- lahjakortti ---
def build_lahjakortti():
    body = (
        sivuotsikko("Lahjaksi läheiselle", "Apua, joka oikeasti helpottaa arkea",
                    "Asutko eri paikkakunnalla kuin vanhempasi? Anna lahjaksi tuttu auttaja, jolle voi soittaa silloinkin kun sinä et ehdi.")
        + '<section class="osio"><div class="sisalto reveal">'
          '<p>Toistuvatko samat puhelut: <em>"taas tämä puhelin tekee jotain outoa"</em> – etkä '
          'pysty auttamaan etänä? Tulen paikan päälle, laitan laitteet kuntoon ja opastan käytön '
          'rauhassa ja selkokielellä. Sinä saat mielenrauhan, ja vanhempasi tutun auttajan jatkoa varten.</p>'
          '<div class="paketit">'
          '<div class="paketti"><h3>Lahjakortti – kotikäynti</h3>'
          '<p class="kk-hinta">89 € <small>yksi käynti</small></p><ul>'
          '<li>Yksi palvelu valinnan mukaan</li><li>Esim. puhelin, reititin tai TV kuntoon</li>'
          '<li>Kesto noin tunti</li><li>Opastus rauhassa ja selkokielellä</li></ul>'
          '<a class="nappi toissijainen" href="yhteys.html">Tilaa lahjakortti</a></div>'
          '<div class="paketti suosituin"><span class="leima">Suosituin</span>'
          '<h3>Lahjakortti – laaja käynti</h3><p class="kk-hinta">149 € <small>kaksi tuntia</small></p><ul>'
          '<li>Kaikki kerralla kuntoon</li><li>Laitteet, tunnukset ja tietoturva</li>'
          '<li>Aikaa myös kysymyksille</li><li>Kahden tunnin käynti</li></ul>'
          '<a class="nappi" href="yhteys.html">Tilaa lahjakortti</a></div>'
          '<div class="paketti"><h3>Lahjaksi: Digiturva</h3>'
          '<p class="kk-hinta">24,90 € <small>/ kk, maksat sinä</small></p><ul>'
          '<li>Jatkuva huijausvahti läheisellesi</li><li>Puhelintuki digipulmiin</li>'
          '<li>Voit maksaa jäsenyyden hänen puolestaan</li><li>Ei sitoutumisaikaa</li></ul>'
          '<a class="nappi toissijainen" href="digiturva.html">Lue Digiturvasta</a></div></div>'
          '<h2>Näin se toimii</h2><ol class="vaiheet">'
          '<li><h3>Ota yhteyttä</h3><p>Kerro kenelle lahja tulee ja millaisten laitteiden kanssa '
          'kaivataan apua.</p></li>'
          '<li><h3>Saat lahjakortin</h3><p>Lähetän kauniin lahjakortin sähköpostiisi '
          'tulostettavaksi tai postitse suoraan saajalle.</p></li>'
          '<li><h3>Sovin käynnin</h3><p>Sovin ajan saajan kanssa ja soitan sinulle jälkikäteen, '
          'jos haluat kuulla miten meni.</p></li></ol>'
          '<div class="huomio"><p><strong>Vinkki:</strong> lahjakortti sopii äitienpäivään, '
          'isänpäivään, jouluun ja merkkipäiviin – se on lahja, joka säästää hermoja koko perheeltä.</p></div>'
          '<p><a class="nappi" href="yhteys.html">Tilaa lahjakortti</a></p></div></section>'
    )
    write("lahjakortti.html", page("lahjakortti.html",
        "Lahjakortti – anna digiapua lahjaksi vanhemmillesi | ET Digiapu",
        "Anna äidille tai isälle lahjaksi kotikäynti tai Digiturva-jäsenyys: laitteet kuntoon ja suoja huijauksilta. Sopii äitienpäivään, isänpäivään ja jouluun.",
        body))


# --- minusta ---
def build_minusta():
    proms = (
        kortti("sydan", "Sama tuttu auttaja", "Ei vaihtuvia asentajia eikä puhelinjonoja – aina minä.")
        + kortti("esto", "En myy ylimääräistä", "En liittymiä, en laitteita, en lisäpalveluja, joita et tarvitse.")
        + kortti("lukko", "En kysy pankkitunnuksia", "Tunnukset ja salasanat pysyvät aina vain sinulla.")
        + kortti("puhe", "Selkokielellä", "Kerron hinnan etukäteen, ja jos en pysty auttamaan, käynti ei maksa mitään.")
    )
    body = (
        sivuotsikko("Tutustu auttajaasi", "Minusta",
                    "Sama tuttu ihminen joka kerta – ei vaihtuvia asentajia eikä puhelinjonoja.")
        + '<section class="osio"><div class="sisalto reveal">'
          '<p>Olen <strong>%s</strong>, ja autan ikäihmisiä digilaitteiden ja sähköisen asioinnin '
          'kanssa alueella [Kaupunki].</p>'
          '<p>Moni on huomannut saman: pankki, Kela ja jopa oma terveysasema hoituvat nykyään '
          'netissä, mutta kukaan ei ehdi opastaa. Omat lapset asuvat kaukana tai vaihtavat '
          'asetukset nopeasti puolestasi – ja ensi viikolla olet taas yksin saman pulman kanssa.</p>'
          '<p>Minä teen toisin. Istun viereesi, etenemme sinun tahdissasi ja kokeilet itse, niin '
          'että opit – sama asia kerrataan niin monta kertaa kuin tarvitaan. Autan sinua kuin '
          'auttaisin omia vanhempiani.</p>'
          '<p>Taustallani on kuusi vuotta työtä asiakkaiden kanssa, joten osaan selittää asiat '
          'ilman tietokonekieltä. Tärkeintä ei ole tekniikka vaan se, että sinulla on rauhallinen '
          'ja turvallinen olo.</p>'
          '<h2>Lupaukseni sinulle</h2><ul class="korttilista">' % NIMI
        + proms +
          '</ul><p><a class="nappi" href="yhteys.html">Soita minulle – jutellaan</a></p></div></section>'
    )
    write("minusta.html", page("minusta.html",
        "Minusta – ET Digiapu",
        "Tutustu auttajaasi: kuusi vuotta asiakaspalvelukokemusta ja aito halu auttaa ikäihmisiä digiasioissa. Sama tuttu auttaja joka kerta, selkokielellä.",
        body, active="minusta.html"))


# --- yhteys ---
def build_yhteys():
    body = (
        sivuotsikko("Ota yhteyttä", "Soita, niin sovitaan",
                    "Helpoin tapa on soittaa – vastaan arkisin klo 9–18. Jos en pääse vastaamaan, soitan takaisin saman päivän aikana.")
        + '<section class="osio"><div class="sisalto reveal">'
          '<div class="kaista"><a class="puhelin-iso" href="tel:%s" style="color:#fff">%s %s</a>'
          '<p>Voit myös lähettää viestin WhatsAppilla tai sähköpostilla: '
          '<a href="%s" style="color:#fff">WhatsApp</a> · '
          '<a href="mailto:%s" style="color:#fff">%s</a></p></div>'
          '<h2>Jätä soittopyyntö</h2>'
          '<p>Jos soittaminen ei juuri nyt sovi, jätä numerosi alle, niin soitan sinulle. Tämä '
          'sopii hyvin myös, jos tilaat apua vanhemmallesi tai haluat liittyä Digiturva-jäseneksi.</p>'
          '<form action="https://formspree.io/f/LOMAKETUNNUS" method="POST">'
          '<label for="nimi">Nimesi</label>'
          '<input type="text" id="nimi" name="nimi" required autocomplete="name">'
          '<label for="puhelin">Puhelinnumerosi</label>'
          '<input type="tel" id="puhelin" name="puhelin" required autocomplete="tel">'
          '<label for="viesti">Missä asiassa tarvitset apua? (vapaaehtoinen)</label>'
          '<textarea id="viesti" name="viesti" rows="4"></textarea>'
          '<div class="suostumus"><input type="checkbox" id="lupa" name="lupa" required>'
          '<label for="lupa">Annan luvan ottaa minuun yhteyttä antamillani tiedoilla. Tietojani '
          'käsitellään <a href="tietosuoja.html">tietosuojaselosteen</a> mukaisesti.</label></div>'
          '<button class="nappi" type="submit">Lähetä soittopyyntö</button></form>'
          '<h2>Epäilyttävä viesti juuri nyt?</h2>'
          '<p>Jos sait viestin, joka epäilyttää, älä klikkaa linkkejä äläkä anna tunnuksia. Ota '
          'kuvakaappaus ja lähetä se minulle WhatsAppilla – tarkistan sen puolestasi. '
          '<a href="digiturva.html">Lue lisää Digiturvasta.</a></p>'
          '<h2>Palvelualue</h2><p>%s. Matkat sisältyvät hintaan palvelualueella – kauempanakin '
          'asuvat voivat kysyä, sovitaan erikseen.</p></div></section>'
    ) % (PUH_NUM, I["puhelin"], PUH_NAYTTO, WA_URL, EMAIL, EMAIL, ALUE)
    write("yhteys.html", page("yhteys.html",
        "Yhteystiedot – ET Digiapu & Digiturva",
        "Soita ja sovi kotikäynti tai liity Digiturva-jäseneksi. Voit myös jättää soittopyynnön, niin soitan takaisin. Palvelualue [Kaupunki] ja lähialueet.",
        body))


# --- vinkit (index) ---
ARTIKKELIT = [
    ("vinkit-huijausviesti.html", "Näin tunnistat huijausviestin",
     "Viisi merkkiä, joista huijausviestin tunnistaa – ja mitä tehdä, jos sait sellaisen."),
    ("vinkit-puhelinhuijaus.html", "Soittiko ”tukihenkilö”? Tee näin",
     "Microsoftin tai pankin nimissä soittavat huijarit ovat yleisiä. Näin toimit oikein."),
    ("vinkit-uusi-puhelin.html", "Vaihdoitko puhelinta? Muista nämä",
     "Tarkistuslista, jolla kuvat, sovellukset ja tunnukset siirtyvät turvallisesti uuteen puhelimeen."),
]


def build_vinkit():
    lista = ""
    for href, otsikko, kuvaus in ARTIKKELIT:
        lista += ('<li class="kortti"><a href="%s"><h3>%s</h3>'
                  '<p class="haalea">%s</p><span class="lue-lisaa">Lue artikkeli →</span></a></li>'
                  ) % (href, otsikko, kuvaus)
    body = (
        sivuotsikko("Vinkit", "Vinkit ja artikkelit",
                    "Selkokielisiä ohjeita huijauksilta suojautumiseen ja arjen digiasioihin. Vapaasti luettavissa.")
        + '<section class="osio"><div class="sisalto reveal">'
          '<ul class="artikkelilista">' + lista + '</ul>'
          '<div class="huomio"><p>Tarvitsetko apua juuri nyt? <a href="yhteys.html">Soita</a> tai '
          'tutustu <a href="digiturva.html">Digiturva-jäsenyyteen</a>, joka tarkistaa epäilyttävät '
          'viestit puolestasi.</p></div></div></section>'
    )
    write("vinkit.html", page("vinkit.html",
        "Vinkit ja artikkelit – ET Digiapu",
        "Selkokielisiä ohjeita huijauksilta suojautumiseen ja arjen digiasioihin: huijausviestit, puhelinhuijaukset ja uuden puhelimen käyttöönotto.",
        body))


def artikkeli(slug, otsikko, kuvaus, sisalto):
    jsonld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
              '"headline":"%s","inLanguage":"fi","author":{"@type":"Person","name":"%s"},'
              '"publisher":{"@type":"Organization","name":"ET Digiapu & Digiturva"}}</script>'
              ) % (otsikko, NIMI)
    body = (
        sivuotsikko("Vinkit", otsikko, kuvaus)
        + '<section class="osio"><div class="sisalto reveal artikkeli">' + sisalto
        + '<div class="huomio turva"><p><strong>Etkö ole varma?</strong> Lähetä kuvakaappaus '
          'epäilyttävästä viestistä WhatsAppilla – <a href="digiturva.html">Digiturva</a> '
          'tarkistaa sen puolestasi. Tai <a href="yhteys.html">soita minulle</a>.</p></div>'
          '<p><a href="vinkit.html">← Takaisin vinkkeihin</a></p></div></section>'
    )
    write(slug, page(slug, otsikko + " – ET Digiapu", kuvaus, body, active="vinkit.html", extra_jsonld=jsonld))


def build_artikkelit():
    artikkeli("vinkit-huijausviesti.html", "Näin tunnistat huijausviestin",
        "Viisi merkkiä, joista huijausviestin tunnistaa – ja mitä tehdä, jos sait sellaisen.",
        '<p>Huijausviestit jäljittelevät yhä taitavammin pankkeja, Postia ja viranomaisia. '
        'Useimmiten ne paljastuvat näistä merkeistä:</p>'
        '<h2>1. Viesti kiirehtii</h2><p>"Toimi heti tai tilisi suljetaan." Kiire on huijarin '
        'tärkein ase – aito taho antaa sinun rauhassa tarkistaa asian.</p>'
        '<h2>2. Linkin osoite on outo</h2><p>Oikea osoite on esimerkiksi <strong>posti.fi</strong>, '
        'ei <strong>posti-fi.xyz</strong> tai <strong>posti.fi.varmistus.com</strong>. Katso '
        'osoitteen loppuosa tarkkaan.</p>'
        '<h2>3. Pyydetään tunnuksia tai korttitietoja</h2><p>Pankki tai viranomainen ei koskaan '
        'pyydä verkkopankkitunnuksia tai kortin numeroa tekstiviestillä tai sähköpostilla.</p>'
        '<h2>4. Kieli on kömpelöä</h2><p>Oudot sanavalinnat, kirjoitusvirheet tai outo suomi '
        'ovat varoitusmerkki.</p>'
        '<h2>5. Et odottanut viestiä</h2><p>Yllättävä "paketti odottaa" tai "olet voittanut" '
        '-viesti palvelusta, jota et käytä, on lähes aina huijaus.</p>'
        '<h2>Mitä tehdä?</h2><ul><li>Älä klikkaa linkkiä äläkä anna mitään tietoja.</li>'
        '<li>Älä vastaa viestiin.</li><li>Poista viesti – tai tarkistuta se ensin.</li>'
        '<li>Jos ehdit jo antaa tietoja, ota heti yhteys pankkiisi.</li></ul>')

    artikkeli("vinkit-puhelinhuijaus.html", "Soittiko ”tukihenkilö”? Tee näin",
        "Microsoftin tai pankin nimissä soittavat huijarit ovat yleisiä. Näin toimit oikein.",
        '<p>Yleinen huijaus on puhelu, jossa "tukihenkilö" väittää tietokoneessasi olevan '
        'ongelman tai pankkisi havainneen epäilyttävää toimintaa. Tavoite on saada sinut '
        'asentamaan etäyhteysohjelma tai kertomaan tunnuksesi.</p>'
        '<h2>Tunnista huijaus</h2><ul>'
        '<li>Soittaja pyytää asentamaan ohjelman tai antamaan etäyhteyden koneellesi.</li>'
        '<li>Soittaja kysyy verkkopankkitunnuksia tai vahvistuskoodeja.</li>'
        '<li>Soittaja painostaa toimimaan heti.</li></ul>'
        '<h2>Toimi näin</h2><ol><li>Sulje puhelin rauhassa – sinun ei tarvitse olla kohtelias '
        'huijarille.</li><li>Älä asenna mitään äläkä anna mitään tunnuksia.</li>'
        '<li>Jos annoit tietoja tai päästit koneelle, sammuta kone ja soita pankkiisi.</li>'
        '<li>Voit tehdä ilmoituksen poliisille.</li></ol>'
        '<p>Aito pankki tai Microsoft ei koskaan soita ja pyydä tunnuksiasi tai etäyhteyttä.</p>')

    artikkeli("vinkit-uusi-puhelin.html", "Vaihdoitko puhelinta? Muista nämä",
        "Tarkistuslista, jolla kuvat, sovellukset ja tunnukset siirtyvät turvallisesti uuteen puhelimeen.",
        '<p>Uuden puhelimen käyttöönotto jännittää monia – pelkona on, että kuvat tai yhteystiedot '
        'katoavat. Näin siirrät tärkeimmät turvallisesti.</p>'
        '<h2>Ennen vaihtoa</h2><ul><li>Varmista, että vanhan puhelimen tiedot on varmuuskopioitu '
        '(iPhonessa iCloud, Androidissa Google-tili).</li>'
        '<li>Tarkista, että muistat sähköpostin ja sen salasanan – niitä tarvitaan uudessa puhelimessa.</li></ul>'
        '<h2>Siirrettävät asiat</h2><ul><li>Kuvat ja videot</li><li>Yhteystiedot</li>'
        '<li>WhatsApp-viestit ja -ryhmät</li><li>Pankkisovellus ja sen tunnusluku</li>'
        '<li>Tärkeät sovellukset (esim. Yle Areena, bussiliput)</li></ul>'
        '<h2>Vaihdon jälkeen</h2><ul><li>Tarkista, että pääset pankkiin ja sähköpostiin.</li>'
        '<li>Säilytä vanha puhelin muutama viikko, kunnes kaikki varmasti toimii.</li>'
        '<li>Tyhjennä vanha puhelin vasta sitten tehdasasetuksiin, jos luovut siitä.</li></ul>'
        '<p>Jos tämä tuntuu työläältä, teen sen puolestasi kotikäynnillä – mitään ei katoa.</p>')


# --- tietosuoja ---
def build_tietosuoja():
    body = (
        sivuotsikko("Tietosuoja", "Tietosuojaseloste",
                    "Näin käsittelen henkilötietoja. Tietoja kerätään vain sen verran kuin palvelun hoitaminen vaatii.")
        + '<section class="osio"><div class="sisalto reveal artikkeli">'
          '<div class="huomio varoitus"><p><strong>Luonnos:</strong> täydennä hakasulkeissa olevat '
          'kohdat (rekisterinpitäjä, yhteystiedot, käytetyt palvelut) ennen julkaisua. Tämä on '
          'EU:n yleisen tietosuoja-asetuksen (GDPR) mukainen seloste.</p></div>'
          '<h2>1. Rekisterinpitäjä</h2><p>%s, Y-tunnus %s. Yhteys: <a href="mailto:%s">%s</a>, '
          'puhelin <a href="tel:%s">%s</a>.</p>'
          '<h2>2. Mitä tietoja kerätään</h2><p>Soittopyyntö- ja yhteydenottolomakkeen kautta: nimi '
          'ja puhelinnumero sekä vapaaehtoinen viesti. Asiakassuhteessa lisäksi käyntiin liittyvät '
          'tiedot ja laskutustiedot. Digiturva-palvelussa käsittelen lähettämiäsi kuvakaappauksia.</p>'
          '<h2>3. Mihin tietoja käytetään ja millä perusteella</h2><p>Tietoja käytetään '
          'yhteydenottoon, palvelun toteuttamiseen ja laskutukseen. Käsittelyn peruste on '
          'suostumuksesi (yhteydenotto) sekä asiakassopimuksen valmistelu ja täyttäminen. '
          'Tietoja ei käytetä markkinointiin ilman erillistä lupaa eikä luovuteta ulkopuolisille.</p>'
          '<h2>4. Kuvakaappausten käsittely (Digiturva)</h2><p>Lähettämäsi kuvat voivat sisältää '
          'henkilötietoja. Ne käsitellään luottamuksellisesti ja vain huijauksen arviointia '
          'varten, ja ne poistetaan, kun asia on käsitelty. <strong>En koskaan pyydä tai tallenna '
          'pankkitunnuksia tai maksukortin tietoja.</strong> Älä lähetä kuvissa tunnuslukuja.</p>'
          '<h2>5. Säilytysaika</h2><p>Yhteydenottotietoja säilytetään vain niin kauan kuin asian '
          'hoitaminen vaatii. Lakisääteiset laskutustiedot säilytetään kirjanpitolain edellyttämän '
          'ajan.</p>'
          '<h2>6. Tietojen sijainti ja käsittelijät</h2><p>[Täydennä käytetyt palvelut, esim. '
          'lomake- ja laskutuspalvelu. Suosi EU-/ETA-alueella toimivia palveluita. Jos käytät AI- '
          'tai pilvipalvelua kuvien analysointiin, varmista käsittelysopimus ja EU-sijainti.]</p>'
          '<h2>7. Sinun oikeutesi</h2><p>Sinulla on oikeus tarkastaa sinusta tallennetut tiedot, '
          'pyytää niiden korjaamista tai poistamista sekä peruuttaa suostumuksesi. Ota yhteyttä '
          'yllä oleviin yhteystietoihin. Voit myös tehdä valituksen tietosuojavaltuutetun '
          'toimistolle (tietosuoja.fi).</p>'
          '<p><a class="nappi toissijainen" href="yhteys.html">Ota yhteyttä</a></p></div></section>'
    ) % (NIMI, YTUNNUS, EMAIL, EMAIL, PUH_NUM, PUH_NAYTTO_TAVALLINEN)
    write("tietosuoja.html", page("tietosuoja.html",
        "Tietosuojaseloste – ET Digiapu",
        "Näin ET Digiapu käsittelee henkilötietoja GDPR:n mukaisesti. Tietoja kerätään vain palvelun hoitamiseksi, eikä pankkitunnuksia koskaan pyydetä.",
        body, active="tietosuoja.html"))


def main():
    os.makedirs(os.path.join(ROOT, "css"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "js"), exist_ok=True)
    build_index(); build_palvelut(); build_digiturva(); build_hinnat()
    build_lahjakortti(); build_minusta(); build_yhteys(); build_vinkit()
    build_artikkelit(); build_tietosuoja()
    print("Tuotettu %d sivua." % (10 + len(ARTIKKELIT)))


if __name__ == "__main__":
    main()
