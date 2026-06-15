/* Kevyt progressiivinen parannus: esiintulo-animaatiot ja huijaustarkistuksen
   demo. Sivu toimii täysin myös ilman JavaScriptiä – tämä vain elävöittää. */
(function () {
  "use strict";

  var reduced = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // 1) Esiintulo vieritettäessä
  var reveals = document.querySelectorAll(".reveal");
  if (reduced || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("nakyvissa"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("nakyvissa"); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    reveals.forEach(function (el) { io.observe(el); });
  }

  // 2) Mobiilin valikko: hampurilaisnappi avaa/sulkee päävalikon
  var navToggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".navigaatio");
  if (navToggle && nav) {
    var sulje = function () {
      nav.classList.remove("auki");
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "Avaa valikko");
    };
    navToggle.addEventListener("click", function () {
      var auki = nav.classList.toggle("auki");
      navToggle.setAttribute("aria-expanded", auki ? "true" : "false");
      navToggle.setAttribute("aria-label", auki ? "Sulje valikko" : "Avaa valikko");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) { sulje(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("auki")) {
        sulje();
        navToggle.focus();
      }
    });
  }

  // 3) Tukiäly: kevyt skriptattu chat-apuri (toimii kaikilla sivuilla)
  var chat = document.querySelector("[data-tukialy]");
  if (chat) {
    var avausNappi = chat.querySelector(".tukialy-nappi");
    var viestit = chat.querySelector(".tukialy-viestit");
    var pikaAlue = chat.querySelector(".tukialy-pikavalinnat");
    var chatLomake = chat.querySelector(".tukialy-syote");
    var chatKentta = chat.querySelector("#tukialy-kentta");
    var chatSulje = chat.querySelector(".tukialy-sulje");
    var naytto = chat.getAttribute("data-naytto");
    var puh = chat.getAttribute("data-puh");
    var waUrl = chat.getAttribute("data-wa");
    var aloitettu = false;

    var VASTAUKSET = {
      palvelut: { teksti: "Teemme kotonasi mm. puhelimen vaihdon ja tietojen siirron, netin ja reitittimen, TV-boksin, tulostimen ja sähköpostin sekä turvakäynnin huijauksia vastaan. Hinnat ovat kiinteät.", cta: { teksti: "Katso palvelut", href: "palvelut.html" } },
      hinnat: { teksti: "Kotikäynnit maksavat 79–99 €, muu apu 79 €/tunti. Digiturva-jäsenyys alkaa 24,90 €/kk. Työ oikeuttaa kotitalousvähennykseen.", cta: { teksti: "Katso hinnat", href: "hinnat.html" } },
      digiturva: { teksti: "Digiturva on jatkuva huijausvahti: lähetät epäilyttävän viestin kuvan, ja tarkistamme sen puolestasi. 24,90 €/kk, ei sitoutumisaikaa.", cta: { teksti: "Lue Digiturvasta", href: "digiturva.html" } },
      huijaus: { teksti: "Älä klikkaa linkkejä äläkä anna pankkitunnuksia kenellekään. Ota viestistä kuvakaappaus ja lähetä se meille WhatsAppilla, niin tarkistamme sen. Jos asia on kiireellinen, soita " + naytto + ".", cta: { teksti: "Lähetä WhatsAppilla", href: waUrl, blank: true } },
      yhteys: { teksti: "Soita " + naytto + " (arkisin klo 9–18) tai jätä soittopyyntö verkkosivulla. Tulemme kotikäynnille omalla palvelualueellamme.", cta: { teksti: "Yhteystiedot", href: "yhteys.html" } },
      fallback: { teksti: "En osaa vielä vastata tähän, mutta autamme mielellämme. Soita " + naytto + " tai jätä soittopyyntö, niin palaamme asiaan.", cta: { teksti: "Soita " + naytto, href: "tel:" + puh } }
    };
    var PIKA = [["Palvelut", "palvelut"], ["Hinnat", "hinnat"], ["Digiturva", "digiturva"], ["Onko tämä huijaus?", "huijaus"], ["Yhteystiedot", "yhteys"]];

    function lisaaKupla(teksti, kuka, cta) {
      var k = document.createElement("div");
      k.className = "tukialy-kupla " + kuka;
      k.textContent = teksti;
      if (cta) {
        k.appendChild(document.createElement("br"));
        var a = document.createElement("a");
        a.className = "tukialy-cta";
        a.href = cta.href;
        a.textContent = cta.teksti;
        if (cta.blank) { a.target = "_blank"; a.rel = "noopener"; }
        k.appendChild(a);
      }
      viestit.appendChild(k);
      viestit.scrollTop = viestit.scrollHeight;
    }

    function botVastaa(aihe) {
      var v = VASTAUKSET[aihe] || VASTAUKSET.fallback;
      if (reduced) { lisaaKupla(v.teksti, "botti", v.cta); return; }
      var ind = document.createElement("div");
      ind.className = "tukialy-kirjoittaa";
      ind.innerHTML = "<span></span><span></span><span></span>";
      viestit.appendChild(ind);
      viestit.scrollTop = viestit.scrollHeight;
      setTimeout(function () { ind.remove(); lisaaKupla(v.teksti, "botti", v.cta); }, 700);
    }

    function tunnista(t) {
      t = t.toLowerCase();
      if (/huijaus|huijar|epäily|epaily|petos|scam|tekstiviest/.test(t)) return "huijaus";
      if (/digiturva|jäsen|jasen|vahti|tilaus/.test(t)) return "digiturva";
      if (/hinta|hinnat|maksa|paljonko|euro|€|kustann|halpa/.test(t)) return "hinnat";
      if (/soita|yhteys|numero|aika|varaa|osoite|missä|missa|alue|sähköpost|sahkopost/.test(t)) return "yhteys";
      if (/palvelu|puhelin|netti|reititin|wifi|televisio|boksi|tulostin|laite|asenn|siirr/.test(t)) return "palvelut";
      return "fallback";
    }

    function kysy(nayttoteksti, aihe) { lisaaKupla(nayttoteksti, "kayttaja"); botVastaa(aihe); }

    function aloita() {
      if (aloitettu) return;
      aloitettu = true;
      lisaaKupla("Hei! Olen Tukiäly, eTukin automaattinen apuri. Voin kertoa palveluista, hinnoista ja Digiturvasta – tai auttaa epäilyttävän viestin kanssa. Mitä haluat tietää?", "botti");
      PIKA.forEach(function (p) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "tukialy-pika"; b.textContent = p[0];
        b.addEventListener("click", function () { kysy(p[0], p[1]); });
        pikaAlue.appendChild(b);
      });
    }

    avausNappi.addEventListener("click", function () {
      chat.classList.add("auki");
      avausNappi.setAttribute("aria-expanded", "true");
      aloita();
      chatKentta.focus();
    });
    function suljeChat() {
      chat.classList.remove("auki");
      avausNappi.setAttribute("aria-expanded", "false");
      avausNappi.focus();
    }
    chatSulje.addEventListener("click", suljeChat);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && chat.classList.contains("auki")) { suljeChat(); }
    });
    chatLomake.addEventListener("submit", function (e) {
      e.preventDefault();
      var arvo = chatKentta.value.trim();
      if (!arvo) return;
      chatKentta.value = "";
      kysy(arvo, tunnista(arvo));
    });
  }

  // 4) Huijaustarkistuksen demo: paljasta kuplat vuoron perään, toista
  var demo = document.querySelector(".demo");
  if (!demo) return;
  var kuplat = Array.prototype.slice.call(demo.querySelectorAll(".kupla"));
  if (!kuplat.length) return;

  if (reduced) { kuplat.forEach(function (k) { k.classList.add("nakyvissa"); }); return; }

  function nayta(i) {
    if (i >= kuplat.length) {
      setTimeout(function () {
        kuplat.forEach(function (k) { k.classList.remove("nakyvissa"); });
        setTimeout(function () { nayta(0); }, 600);
      }, 4200);
      return;
    }
    kuplat[i].classList.add("nakyvissa");
    setTimeout(function () { nayta(i + 1); }, 1100);
  }

  if ("IntersectionObserver" in window) {
    var started = false;
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && !started) { started = true; nayta(0); }
      });
    }, { threshold: 0.4 });
    io2.observe(demo);
  } else {
    nayta(0);
  }
})();
