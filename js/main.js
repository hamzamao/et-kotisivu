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

  // 2) Huijaustarkistuksen demo: paljasta kuplat vuoron perään, toista
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
