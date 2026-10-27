(function () {
  var btn = document.getElementById('burger');
  var nav = document.getElementById('nav');
  if (!btn || !nav) return;
  function setOpen(open) {
    nav.classList.toggle('is-open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  }
  btn.addEventListener('click', function () { setOpen(!nav.classList.contains('is-open')); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); btn.focus(); }
  });
  window.addEventListener('resize', function () { if (window.innerWidth > 980) setOpen(false); });
})();

(function () {
  var form = document.getElementById('form');
  if (!form) return;
  var PHONE = '+33679799405';
  var recap = document.getElementById('recap');
  var out = document.getElementById('recap-text');
  var status = document.getElementById('recap-status');
  var rules = {
    nom: function (v) { return v.trim().length >= 2 ? '' : 'Indiquez votre nom.'; },
    tel: function (v) { return /^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$/.test(v.trim()) ? '' : 'Indiquez un numéro valide, par exemple 06 12 34 56 78.'; },
    commune: function (v) { return v.trim().length >= 2 ? '' : 'Indiquez votre commune.'; },
    besoin: function (v) { return v ? '' : 'Choisissez un besoin dans la liste.'; }
  };
  function check(name) {
    var el = form.elements[name], err = document.getElementById('e-' + name);
    var msg = rules[name](el.value);
    err.textContent = msg; err.hidden = !msg;
    if (msg) { el.setAttribute('aria-invalid', 'true'); } else { el.removeAttribute('aria-invalid'); }
    return !msg;
  }
  Object.keys(rules).forEach(function (n) {
    form.elements[n].addEventListener('blur', function () { check(n); });
    form.elements[n].addEventListener('input', function () { if (form.elements[n].getAttribute('aria-invalid')) check(n); });
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var first = null;
    Object.keys(rules).forEach(function (n) { if (!check(n) && !first) first = form.elements[n]; });
    if (first) { first.focus(); return; }
    var f = form.elements;
    var txt = 'Demande de contact pour Artivert Lenaik\nNom : ' + f.nom.value.trim() + '\nTéléphone : ' + f.tel.value.trim() + '\nCommune : ' + f.commune.value.trim() + '\nBesoin : ' + f.besoin.value;
    if (f.message.value.trim()) txt += '\nMessage : ' + f.message.value.trim();
    out.value = txt;
    document.getElementById('btn-sms').href = 'sms:' + PHONE + '?&body=' + encodeURIComponent(txt);
    status.textContent = 'Votre demande est prête. Elle n\'est pas encore envoyée : choisissez un moyen ci-dessous.';
    form.hidden = true; recap.hidden = false; recap.focus();
  });
  document.getElementById('btn-edit').addEventListener('click', function () {
    recap.hidden = true; form.hidden = false; form.elements.nom.focus();
  });
  document.getElementById('btn-copy').addEventListener('click', function () {
    var b = this;
    function done(ok) { status.textContent = ok ? 'Texte copié. Collez-le dans un message.' : 'Copie impossible : sélectionnez le texte et copiez-le.'; }
    function fallback() { out.focus(); out.select(); var ok = false; try { ok = document.execCommand('copy'); } catch (x) {} done(ok); }
    if (navigator.clipboard && navigator.clipboard.writeText) { navigator.clipboard.writeText(out.value).then(function () { done(true); }, fallback); } else { fallback(); }
  });
})();
