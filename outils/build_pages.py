import re, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx = open(R + "/index.html", encoding="utf-8").read()
HEAD_FONTS = re.search(r'<link rel="icon".*?<link rel="stylesheet" href="css/style.css">', idx, re.S).group(0)
HDR = re.search(r'<header class="hdr">.*?</header>', idx, re.S).group(0)
FTR = re.search(r'<footer class="ftr">.*?</footer>', idx, re.S).group(0)
HDR = HDR.replace(' aria-current="page"', "")
PHONE_SVG = re.search(r'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16\.9.*?</svg>', idx, re.S).group(0)

def page(fname, title, desc, current, main):
    h = HDR.replace('<a href="%s">' % current, '<a href="%s" aria-current="page">' % current, 1)
    html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
{HEAD_FONTS}
</head>
<body>
{h}

<main>
{main}
</main>

{FTR}
<script src="js/main.js"></script>
</body>
</html>
'''
    open(R + "/" + fname, "w", encoding="utf-8").write(html)

CALL = f'<a class="btn btn--leaf" href="tel:+33679799405">{PHONE_SVG}Appeler le 06 79 79 94 05</a>'

PRESTA = f'''<section class="phead" aria-labelledby="h1">
  <div class="wrap phead__in">
    <div>
      <p class="eyebrow">Prestations</p>
      <h1 id="h1">Aménager et entretenir votre jardin</h1>
      <p class="lead">Terrasses, allées, murets, plantations, tonte et taille : Artivert Lenaik intervient de la création du jardin jusqu'à son entretien.</p>
      <div class="hero__cta">
        {CALL}
        <a class="btn btn--ghost" href="contact.html">Décrire mon projet</a>
      </div>
    </div>
    <div class="mosaic">
      <figure><img src="images/terrasse-bois.jpg" width="1000" height="545" alt="Illustration : terrasse en bois en cours de pose devant une maison en pierre" fetchpriority="high"></figure>
      <figure><img src="images/allee-dallee.jpg" width="1000" height="545" alt="Illustration : allée dallée éclairée en soirée le long d'une maison"></figure>
      <figure><img src="images/maconnerie.jpg" width="1000" height="545" alt="Illustration : muret de pierres et escalier de jardin en cours de construction"></figure>
    </div>
  </div>
</section>

<section class="sec sec--stone sec--under" id="amenager" aria-labelledby="h-amenager">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">Aménager</p>
      <h2 id="h-amenager">Du terrain brut au jardin où l'on vit</h2>
    </div>
    <div class="rows">
      <article class="row">
        <figure><img src="images/creation.jpg" width="1000" height="545" loading="lazy" alt="Illustration : création d'un espace vert"></figure>
        <div>
          <h3>Création d'espaces verts</h3>
          <p>Pelouse, massifs, plantations : le jardin est conçu pour la maison, l'exposition et l'usage que vous en avez.</p>
        </div>
      </article>
      <article class="row row--rev">
        <figure><img src="images/nivellement.jpg" width="1000" height="546" loading="lazy" alt="Illustration : nivellement d'un terrain de jardin"></figure>
        <div>
          <h3>Terrassement et nivellement</h3>
          <p>Un sol préparé avec soin donne des terrasses, des allées et des pelouses qui durent.</p>
        </div>
      </article>
    </div>
    <ul class="chips">
      <li>Terrasses en bois</li><li>Allées et dallages</li><li>Maçonnerie paysagère</li><li>Plantations</li>
    </ul>
  </div>
</section>

<section class="sec sec--lift on-band" id="entretenir" aria-labelledby="h-entretenir">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Entretenir</p>
      <h2 id="h-entretenir">Un jardin qui reste soigné toute l'année</h2>
      <p class="mut">L'entretien suit le jardin au fil des saisons, avec les mêmes interlocuteurs que pour sa création.</p>
      <ul class="checks">
        <li>Tonte des pelouses</li><li>Taille de haies</li><li>Désherbage</li><li>Ramassage des feuilles</li><li>Évacuation des déchets verts</li>
      </ul>
    </div>
    <div class="pair">
      <img src="images/tonte.jpg" width="1000" height="558" loading="lazy" alt="Illustration : tonte d'une pelouse">
      <img src="images/taille-haies.jpg" width="1000" height="747" loading="lazy" alt="Illustration : taille d'une haie">
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="h-strip">
  <div class="wrap">
    <div class="strip">
      <p class="eyebrow" style="color:inherit">Votre projet</p>
      <h2 id="h-strip">Un jardin à aménager ou à entretenir ?</h2>
      <p>Appelez directement ou décrivez votre jardin en quelques lignes.</p>
      <div class="cta__row">
        <a class="btn btn--dark" href="tel:+33679799405">06 79 79 94 05</a>
        <a class="btn btn--ghost" href="tel:+33139125406">01 39 12 54 06</a>
        <a class="btn btn--ghost" href="contact.html">Décrire mon projet</a>
      </div>
    </div>
  </div>
</section>'''

ENTR = f'''<section class="ehead on-band" aria-labelledby="h1">
  <div class="wrap ehead__in">
    <div>
      <p class="eyebrow">L'entreprise</p>
      <h1 id="h1">Une entreprise de paysage basée à Houilles</h1>
      <ul class="stats">
        <li><b>2002</b>année de création</li>
        <li><b>10 à 19</b>salariés en 2024</li>
        <li><b>SARL</b>forme juridique</li>
        <li><b>Houilles</b>Yvelines, 78</li>
      </ul>
    </div>
    <figure><img src="images/robot-tonte.jpg" width="1000" height="545" alt="Illustration : jardin aménagé avec pelouse, massifs, muret de pierres et terrasse"></figure>
  </div>
</section>

<section class="sec" aria-labelledby="h-reperes">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">Repères</p>
      <h2 id="h-reperes">Plus de vingt ans d'existence</h2>
    </div>
    <ol class="timeline">
      <li><time>1er juin 2002</time><p>Inscription de la société au répertoire de l'Insee.</p></li>
      <li><time>28 juin 2002</time><p>Immatriculation au registre national des entreprises.</p></li>
      <li><time>2024</time><p>L'entreprise compte entre 10 et 19 salariés et relève de la catégorie des PME.</p></li>
      <li><time>Aujourd'hui</time><p>Société en activité, avec son siège au 42 avenue de l'Yser, à Houilles.</p></li>
    </ol>
  </div>
</section>

<section class="sec sec--stone" aria-labelledby="h-dir">
  <div class="wrap dir">
    <figure>
      <img src="images/conception.jpg" width="1000" height="545" loading="lazy" alt="Illustration : plan de jardin affiché sur une tablette">
      <figcaption>Illustration. Du plan au jardin planté.</figcaption>
    </figure>
    <div class="card">
      <p class="eyebrow">Direction</p>
      <h2 id="h-dir">Rodolphe Gaffet</h2>
      <p>Rodolphe Gaffet dirige Artivert Lenaik. C'est avec lui et son équipe que vous échangez, de la visite du jardin jusqu'à l'entretien.</p>
      <p class="src" style="margin-top:16px;color:var(--muted)">Source : Annuaire des entreprises.</p>
    </div>
  </div>
</section>

<section class="sec sec--lift on-band" aria-labelledby="h-find">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">Nous joindre</p>
      <h2 id="h-find">Un projet ? Parlons-en</h2>
    </div>
    <div class="find">
      <div class="card">
        <h3>Par téléphone</h3>
        <a class="tel" href="tel:+33679799405">06 79 79 94 05</a>
        <a class="tel" href="tel:+33139125406">01 39 12 54 06</a>
      </div>
      <div class="card">
        <h3>Siège de l'entreprise</h3>
        <address>Artivert Lenaik<br>42 avenue de l'Yser<br>78800 Houilles</address>
        <p style="margin-top:16px"><a class="btn btn--dark" href="contact.html">Décrire mon projet</a></p>
      </div>
    </div>
  </div>
</section>'''

CONT = f'''<section class="sec sec--stone sec--under" aria-labelledby="h1">
  <div class="wrap">
    <div class="sec__head">
      <p class="eyebrow">Contact</p>
      <h1 id="h1" style="font-size:clamp(2rem,5vw,3.25rem)">Décrivez-nous votre projet</h1>
      <p>Remplissez ces quelques champs : nous préparons un message prêt à envoyer par SMS, ou appelez directement.</p>
    </div>
    <div class="cinfo">
      <div class="card">
        <h2>Nous appeler</h2>
        <a class="tel" href="tel:+33679799405">06 79 79 94 05</a>
        <a class="tel" href="tel:+33139125406">01 39 12 54 06</a>
      </div>
      <div class="card">
        <h2>Siège</h2>
        <address style="font-style:normal;font-weight:600">Artivert Lenaik<br>42 avenue de l'Yser<br>78800 Houilles</address>
      </div>
      <div class="card">
        <h2>Comment ça marche</h2>
        <ol><li>Vous remplissez le formulaire.</li><li>Vous vérifiez le récapitulatif.</li><li>Vous l'envoyez par SMS ou vous appelez.</li></ol>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--lift on-band" id="formulaire" aria-labelledby="h-form">
  <div class="wrap">
    <div class="cform">
        <form class="card form" id="form" novalidate>
          <h2 id="h-form" style="font-size:1.5rem">Votre demande</h2>
          <div class="field"><label for="f-nom">Nom</label><input id="f-nom" name="nom" type="text" autocomplete="name" required aria-describedby="e-nom"><p class="err" id="e-nom" role="alert" hidden></p></div>
          <div class="field"><label for="f-tel">Téléphone</label><input id="f-tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" required aria-describedby="e-tel"><p class="err" id="e-tel" role="alert" hidden></p></div>
          <div class="field"><label for="f-commune">Commune</label><input id="f-commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="e-commune"><p class="err" id="e-commune" role="alert" hidden></p></div>
          <div class="field"><label for="f-besoin">Votre besoin</label>
            <select id="f-besoin" name="besoin" required aria-describedby="e-besoin">
              <option value="">Choisir dans la liste</option>
              <option>Création d'un jardin ou d'un espace vert</option>
              <option>Terrasse ou allée</option>
              <option>Maçonnerie paysagère</option>
              <option>Plantations</option>
              <option>Entretien du jardin</option>
              <option>Autre demande</option>
            </select><p class="err" id="e-besoin" role="alert" hidden></p></div>
          <div class="field"><label for="f-message">Message (facultatif)</label><textarea id="f-message" name="message" rows="4"></textarea></div>
          <button class="btn btn--leaf btn--block" type="submit">Préparer ma demande</button>
        </form>
        <div class="card recap" id="recap" tabindex="-1" hidden style="margin-top:20px">
          <h2 style="font-size:1.5rem">Demande prête</h2>
          <p class="ok" id="recap-status" role="status"></p>
          <textarea id="recap-text" readonly aria-label="Récapitulatif de votre demande"></textarea>
          <div class="recap__btns">
            <a class="btn btn--leaf" id="btn-sms" href="sms:+33679799405">Envoyer par SMS</a>
            <button class="btn btn--dark" id="btn-copy" type="button">Copier</button>
            <a class="btn btn--dark" href="tel:+33679799405">Appeler</a>
          </div>
        </div>
      </div>
  </div>
</section>'''

page("prestations.html", "Prestations paysagères à Houilles | Artivert Lenaik",
     "Artivert Lenaik à Houilles : création d'espaces verts, terrasses, allées, maçonnerie paysagère, plantations et entretien de jardins.", "prestations.html", PRESTA)
page("entreprise.html", "L'entreprise | Artivert Lenaik, Houilles",
     "Artivert Lenaik, entreprise d'aménagement paysager créée en 2002 et basée à Houilles, dans les Yvelines.", "entreprise.html", ENTR)
page("contact.html", "Contact | Artivert Lenaik, Houilles",
     "Contactez Artivert Lenaik à Houilles : téléphone, adresse du siège et formulaire de demande de contact.", "contact.html", CONT)
