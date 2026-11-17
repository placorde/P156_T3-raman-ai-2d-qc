# Literature review — v0.2 (recherche bibliographique)

> v0.1 (2026-10-06) : premier passage "chercheur" avant le kick-off partenaire — physique de
> base, datasets, état de l'art ML/DL.
> v0.2 (2026-11-17) : deuxième passage, ciblé sur le **code open-source réutilisable** et les
> **datasets supplémentaires** (sections 7-9). Voir aussi le statut du kick-off : au
> 2026-11-17, rien n'indique qu'il ait eu lieu (toujours en attente de confirmation côté
> équipe).

## 1. Physique : ce que dit un spectre Raman

Chaque matériau 2D a une signature Raman caractéristique :

- **Graphène / graphite** : bande **D** (~1350 cm⁻¹, activée par le désordre), bande **G**
  (~1580 cm⁻¹, mode E2g du réseau sp²), bande **2D** (~2700 cm⁻¹, harmonique de la bande D,
  active même sans défaut). La **forme** et l'**intensité relative** de la bande 2D renseignent
  sur le nombre de couches (mono- vs bi- vs multi-couche).
- **h-BN** : un seul mode Raman actif dominant (E2g, ~1366 cm⁻¹) — signature simple mais peu
  de redondance pour la classification.
- **TMDs (MoS₂, WS₂, MoSe₂, WSe₂)** : deux modes principaux, **E2g¹** (in-plane) et **A1g**
  (out-of-plane), dont l'écart en fréquence est lui-même un indicateur du nombre de couches.

### Indicateurs de qualité déjà établis dans la littérature

- **I(D)/I(G)** : métrique standard de densité de défauts pour les matériaux carbonés. **Attention,
  relation non monotone** : le ratio augmente avec la densité de défauts jusqu'à un maximum,
  puis **redescend** aux densités de défauts élevées (régime amorphe). Un score "qualité" basé
  uniquement sur I(D)/I(G) sans préciser le régime peut donc être ambigu — à mentionner
  explicitement dans le rapport et à poser comme question à la partenaire (§3 du cahier des
  charges).
- **I(2D)/I(G)** : pour du graphène monocouche de bonne qualité, ce ratio vaut typiquement ~2 ;
  il diminue avec le nombre de couches / le désordre.
- Position et largeur à mi-hauteur (FWHM) des bandes D/G/2D : sensibles au dopage, aux
  contraintes mécaniques et aux interactions avec le substrat, en plus des défauts — donc pas
  un indicateur "pur" de qualité si utilisé isolément.
- Revue récente et critique sur la bande D : *Revisiting the Raman disorder band in
  graphene-based materials* (ScienceDirect, 2025) — bonne entrée pour nuancer un indicateur de
  qualité simpliste dans le rapport scientifique.

→ **Implication pour le projet** : l'indicateur de qualité (item 6 du sujet) ne doit probablement
pas être un simple seuil sur I(D)/I(G), mais soit (a) restreint à un régime de défauts
faible/modéré (hypothèse à valider avec la partenaire), soit (b) une combinaison de plusieurs
features (ratios + FWHM + position) apprise plutôt que fixée à la main.

## 2. Jeux de données exploitables

| Source | Type | Contenu | Licence/accès | Remarque |
|---|---|---|---|---|
| [C2DB — library of ab initio Raman spectra](https://www.nature.com/articles/s41467-020-16529-6) ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7296020/), [arXiv](https://arxiv.org/html/2001.06313v3)) | **Simulé** (DFT) | Spectres Raman calculés pour 733 monocouches, dont graphène, h-BN, TMDs H/T′, phosphorène. Procédure automatique d'identification de matériau à partir d'un spectre. | Base C2DB ouverte (c2db.fysik.dtu.dk) | Pas de bruit expérimental réel — utile comme base d'identification/pré-entraînement, pas comme seul jeu de test. |
| [Deep learning assisted Raman spectroscopy for rapid identification of 2D materials](https://arxiv.org/pdf/2312.01389) ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S235294072400444X)) | **Expérimental + augmenté** | 594 spectres Raman réels pour 7 matériaux 2D (BP, graphène, MoS₂, ReS₂, Te, WSe₂, WTe₂) + 3 empilements, augmentés via DDPM (10 000 spectres synthétiques) ; CNN 4 couches ; 100% accuracy annoncée. | À vérifier (article en accès payant/arXiv preprint dispo) | **Le plus proche du scope du sujet** — à lire en détail, sert de référence directe pour le choix d'architecture et la stratégie d'augmentation. |
| [Raman and photoluminescence of MoS₂ flakes and pyramids (Zenodo)](https://zenodo.org/records/5866629) | Expérimental réel | Spectres Raman + PL de MoS₂ | CC BY 4.0 | Directement réutilisable, licence claire. |
| RamanBench (benchmark agrégateur, HuggingFace/Kaggle/Zenodo) | Mixte | Agrège de nombreux jeux de données Raman, dont matériaux | À vérifier par dataset | Bon point de départ pour explorer large avant de choisir. |
| MLROD (Mars minerals) | Expérimental réel | 89 121 spectres, 12 minéraux | Hors-sujet matériaux 2D | Pas pour l'entraînement, mais bon exemple de méthodologie de benchmark à grande échelle. |

**Piste de stratégie** : combiner (a) les spectres *ab initio* C2DB pour couvrir un grand nombre
de matériaux/familles et stabiliser l'entraînement, (b) les 594 spectres expérimentaux +
augmentation (DDPM ou perturbations synthétiques plus simples : bruit, décalage, variation
d'intensité — ce que demande justement le point 5 du sujet) pour le réalisme, (c) Zenodo MoS₂
pour un test indépendant sur données réelles. À confirmer avec la partenaire si elle a déjà une
source de données "maison" à privilégier (question posée dans le cahier des charges).

## 3. Outillage existant pour le prétraitement (ne pas tout réinventer)

- **[RamanSPy](https://ramanspy.readthedocs.io/)** ([ACS Anal. Chem. 2024](https://pubs.acs.org/doi/10.1021/acs.analchem.4c00383), [bioRxiv](https://www.biorxiv.org/content/10.1101/2023.07.05.547761v1.full)) : package Python moderne et maintenu — denoising, correction de ligne de base (AsLS, IAsLS, airPLS, arPLS, polynomiale), suppression des spikes cosmiques, normalisation, chargement de données, visualisation. **Candidat naturel** pour la brique "prétraitement" du pipeline (item 1 du sujet) plutôt que tout recoder.
- **[RamPy](https://github.com/charlesll/rampy)** ([doc peak fitting](https://rampy.readthedocs.io/en/stable/notebooks/Raman_fitting.html)) : plus léger, bon pour le fitting de pics (via lmfit) — utile pour l'extraction de features physiques (position/largeur/intensité, item 2 du sujet).

→ Recommandation : s'appuyer sur RamanSPy pour le prétraitement standard, et ne développer en
propre que ce qui est spécifique au projet (détection de pics adaptée aux bandes D/G/2D,
indicateur de qualité, pipeline de classification).

## 4. État de l'art ML/DL — ce qui marche en pratique

- Les **1D-CNN et variantes ResNet** dominent la littérature récente pour la classification de
  spectres Raman ; les baselines classiques (KNN, SVM, Random Forest) restent des points de
  comparaison standards — exactement la comparaison demandée au point 4 du sujet.
- Revues utiles à citer dans le rapport scientifique :
  - [Recent Advances in Raman Spectral Classification with Machine Learning (MDPI Sensors)](https://www.mdpi.com/1424-8220/26/1/341)
  - [Deep Learning for Raman Spectroscopy: A Review (MDPI)](https://www.mdpi.com/2673-4532/3/3/20)
  - [Advances in deep learning-based applications for Raman spectroscopy analysis (2025, mini-review)](https://www.sciencedirect.com/science/article/abs/pii/S0026265X25000463)
  - [Benchmarking deep learning models for Raman spectroscopy across open-source datasets (RSC Digital Discovery)](https://pubs.rsc.org/dd/article/5/8/3314/1277710/Benchmarking-deep-learning-models-for-Raman)
- Constat récurrent : les jeux de données réels sont **petits et déséquilibrés** → l'augmentation
  de données (bruit synthétique, décalages spectraux, modèles génératifs type DDPM) est
  systématiquement utilisée pour stabiliser l'entraînement des CNN. Ça correspond directement au
  point 5 du sujet (robustesse au bruit/décalage/intensité) : on peut traiter l'augmentation de
  données et l'évaluation de robustesse comme **deux faces du même mécanisme**.
- Les CNN 1D sont rapportés plus robustes que les modèles classiques quand les spectres sont
  bruités (faible puissance laser / temps d'intégration court) — argument direct pour justifier
  la comparaison ML vs DL demandée par le sujet, pas juste une case à cocher.

## 5. Questions que cette recherche ajoute pour la partenaire

À ajouter à la section 3 du `cahier_des_charges.md` :

- A-t-elle une préférence entre s'appuyer sur des spectres *ab initio* (C2DB) en complément des
  données réelles, ou veut-elle qu'on reste strictement sur données expérimentales ouvertes ?
- Le régime de densité de défauts visé pour l'indicateur qualité est-il plutôt faible/modéré
  (où I(D)/I(G) est monotone) ou doit-on couvrir aussi le régime fortement désordonné ?
- Accepte-t-elle qu'on s'appuie sur RamanSPy/RamPy pour le prétraitement standard, ou attend-elle
  une implémentation "from scratch" des étapes de prétraitement pour des raisons pédagogiques ?

## 7. Code open-source directement réutilisable (repos GitHub, recherche 2026-11-17)

| Repo | Ce qu'il fait | Données | Licence | État |
|---|---|---|---|---|
| [Surjyasish/Raman-mapping-graphene](https://github.com/Surjyasish/Raman-mapping-graphene) | Pipeline complet graphène/graphite : stitching, correction de ligne de base (ALS), fitting Lorentzien des bandes D/G/D′/2D/D+G, features I(D)/I(G) et I(2D)/I(G), clustering PCA+k-means, **CNN 1D avec split spatial** (pas aléatoire — argument pédagogique à reprendre), interprétabilité Grad-CAM. | Carte 27×35 µm (945 pixels) décrite dans le README mais **fichiers de données non inclus dans le repo**. | Apache-2.0 | 16 commits, 0 star/fork — pas de communauté, mais c'est **le plus proche structurellement de ce que demande le sujet** (points 1, 2, 3, 6 à la fois). À lire comme référence d'architecture plutôt qu'à exécuter tel quel. |
| [asineesh/Benchmark_Raman_DeepLearning](https://github.com/asineesh/Benchmark_Raman_DeepLearning) | Benchmark PyTorch rigoureux : SVM/Random Forest vs Deep CNN/SANet/RamanNet/Transformer/RamanFormer, même protocole d'entraînement/évaluation pour tous. | 3 datasets déjà scriptés (MLROD via odr.io, Bacteria-ID via GitHub, API pharma via Figshare) — **aucun n'est un matériau 2D**, mais la structure du code (tuning → multi-run → évaluation accuracy/F1) est directement réutilisable pour comparer nos propres modèles. | MIT | Bien structuré, poids/logs archivés sur Zenodo. Bon modèle de **méthodologie de comparaison** pour le point 4 du sujet. |
| [Naduhi/Raman_DL](https://github.com/Naduhi/Raman_DL) | Cité comme dépôt de code de l'article DDPM-CNN (arXiv:2312.01389, le papier le plus proche du sujet). | — | — | **Lien mort / 404 au 2026-11-17** — à retenter plus tard ou à contacter les auteurs directement si on veut leur code. |
| [ml-lab-htw/raman_data](https://github.com/ml-lab-htw/raman_data) | Librairie Python unifiée de chargement de **93 datasets Raman** publics (classification, régression, débruitage, super-résolution), agrégés depuis Kaggle/HuggingFace/Zenodo/Figshare/Mendeley/GitHub. | Aucun matériau 2D listé pour l'instant (voir §8), mais pratique pour explorer/charger rapidement d'autres jeux Raman si besoin de données de pré-entraînement généralistes. | Vérifier par dataset | Lié au papier RamanBench (§8) ; aussi sur PyPI (`pip install raman-data`). |

→ **Aucun repo trouvé n'est un pipeline "clé en main" prêt à l'emploi pour le sujet exact**
(classification de matériaux 2D + indicateur qualité). Le plus utile reste
`Surjyasish/Raman-mapping-graphene` comme **modèle d'architecture** (features physiques +
CNN + interprétabilité), à adapter avec nos propres données plutôt qu'à cloner tel quel.

## 8. Datasets supplémentaires identifiés (recherche 2026-11-17)

| Source | Type | Contenu | Accès |
|---|---|---|---|
| [raman-data (PyPI)](https://pypi.org/project/raman-data/) + [RamanBench (arXiv:2605.02003)](https://arxiv.org/html/2605.02003v2) | Benchmark agrégateur | 74 datasets / 325 000+ spectres au total, mais seulement **4 en "Material Science"** : MLROD (minéraux Mars), RRUFF (minéraux), pigments organiques synthétiques, microplastiques altérés — **aucun n'est un matériau 2D**. | `pip install raman-data` / `raman-bench` ; leaderboard public sur [HuggingFace Spaces](https://huggingface.co/spaces/HTW-KI-Werkstatt/RamanBench) |
| [RamanSPy — datasets intégrés](https://ramanspy.readthedocs.io/en/latest/datasets.html) | Chargeurs prêts à l'emploi | Bactéries, cellules, COVID-19, adénine, blé, et **RRUFF (minéraux)** — aucun matériau 2D non plus, mais utile si on veut tester notre pipeline de prétraitement sur un jeu "neutre" avant de l'appliquer à nos propres spectres. | Intégré à la lib (`rp.datasets.*`) |
| [Malenfant-Thuot et al., *Large Scale Raman Spectrum Calculations in Defective 2D Materials using Deep Learning*, J. Phys.: Condens. Matter 37, 115903 (2025)](https://arxiv.org/abs/2410.20417) | **Simulé** (potentiels interatomiques appris + DFT) | Génère à grande échelle des spectres Raman de **h-BN défectueux** (3 à 8 atomes retirés par configuration) — méthodologiquement très proche du point 6 du sujet (indicateur de défauts), même si c'est du h-BN et pas du carbone. Pas de lien dataset/code confirmé dans les sources consultées — à vérifier directement dans l'article complet (data availability statement). | Papier accessible, dataset/code à confirmer |
| [Cao et al., *From Data to Discovery: ML-Enabled Intelligent Characterization of 2D Materials*, Advanced Intelligent Discovery (2025)](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aidi.70145) | Revue | Vue d'ensemble des méthodes ML pour caractériser des matériaux 2D (pas seulement Raman) — bon point d'entrée bibliographique pour le rapport, mais accès à vérifier (403 rencontré lors de la recherche, probablement paywall). | À vérifier (accès bibliothèque ESILV ?) |
| [Qi et al. — version révisée/publiée, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S235294072400444X) et [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4930953) | Expérimental + DDPM | Confirme les chiffres déjà notés en v0.1 : 594 spectres réels, 7 matériaux + 3 empilements, **CNN seul = 98,8%**, **DDPM+CNN = 100%**. Avoir les deux chiffres (pas juste le 100%) est plus honnête à citer dans notre propre rapport. | Preprint arXiv + versions éditeur |

**Constat net après cette deuxième passe** : il n'existe **pas de dataset expérimental ouvert,
volumineux et dédié aux matériaux 2D** comparable à ce qui existe pour d'autres domaines Raman
(bactéries, minéraux...). Le jeu de 594 spectres (Qi et al.) reste la meilleure base
expérimentale publique identifiée pour ce sujet précis ; le reste (C2DB, Zenodo MoS₂) sert à
compléter. Ça renforce l'argument déjà noté en v0.1 : l'**augmentation de données** n'est pas
une option, c'est une nécessité pour ce projet, quel que soit le dataset de départ choisi.

## 9. Sources ajoutées en v0.2

- [Surjyasish/Raman-mapping-graphene (GitHub)](https://github.com/Surjyasish/Raman-mapping-graphene)
- [asineesh/Benchmark_Raman_DeepLearning (GitHub)](https://github.com/asineesh/Benchmark_Raman_DeepLearning)
- [ml-lab-htw/raman_data (GitHub)](https://github.com/ml-lab-htw/raman_data) / [raman-data (PyPI)](https://pypi.org/project/raman-data/)
- [RamanBench: A Large-Scale Benchmark for Machine Learning on Raman Spectroscopy (arXiv:2605.02003)](https://arxiv.org/html/2605.02003v2)
- [RamanBench leaderboard (HuggingFace Spaces)](https://huggingface.co/spaces/HTW-KI-Werkstatt/RamanBench)
- [RamanSPy — datasets intégrés](https://ramanspy.readthedocs.io/en/latest/datasets.html)
- [Malenfant-Thuot et al., Large Scale Raman Spectrum Calculations in Defective 2D Materials using Deep Learning (arXiv:2410.20417)](https://arxiv.org/abs/2410.20417)
- [Cao et al., From Data to Discovery: ML-Enabled Intelligent Characterization of 2D Materials (Advanced Intelligent Discovery, 2025)](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aidi.70145)
- [Qi et al., version ScienceDirect](https://www.sciencedirect.com/science/article/pii/S235294072400444X) / [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4930953)

## 11. Materials Project, Materials Cloud et la Computational Raman Database (suite recherche 2026-11-17)

À la demande de l'équipe, exploration de [Materials Project](https://next-gen.materialsproject.org/)
et [Materials Cloud](https://www.materialscloud.org/), à partir de liens partagés par l'équipe.

### Materials Project (MP)

Base de données de propriétés de matériaux calculées par DFT (Lawrence Berkeley National
Lab) — structures cristallines, bandes électroniques, propriétés élastiques/piézoélectriques/
diélectriques, phonons, pour des centaines de milliers de composés. **Accès direct au site
bloqué pour nous ici** (protection anti-robot Cloudflare — je n'ai pas essayé de la contourner,
c'est hors limites). Pour une extraction de données réelle, il faut : créer un compte gratuit
sur [materialsproject.org](https://next-gen.materialsproject.org/), récupérer une clé API
personnelle, puis utiliser le client Python officiel `mp-api`
([doc](https://docs.materialsproject.org/downloading-data/how-do-i-download-the-materials-project-database)).
**MP n'héberge pas directement de spectres Raman** pour la plupart des matériaux — c'est surtout
un système d'identifiants (`mp-id`) et de propriétés de structure/électronique sur lequel
d'autres bases Raman (ci-dessous) s'appuient. Filtrer par dimensionnalité (pour isoler les
matériaux 2D) est possible via l'API mais pas encore un filtre de premier niveau d'après un fil
de discussion de la communauté ([matsci.org](https://matsci.org/t/how-to-get-the-2d-material-data-of-material-project/47828)).

### Computational Raman Database (CRD) — [ramandb.oulu.fi](https://ramandb.oulu.fi/)

Base dédiée aux spectres Raman *calculés* (plus de 5000 spectres, semi-conducteurs et
isolants), construite sur la Phonon Database d'Atsushi Togo avec un pré-criblage via
Materials Project — **recherche possible directement par `mp-id` et par dimensionnalité**,
donc un bon pont entre MP et des données Raman exploitables. Chaque fiche matériau donne le
spectre Raman/IR interactif et le tenseur Raman brut. CC BY 4.0, code source sur GitHub
(`ramandb`) et toolkit Python `CoRaPy`. Référence : Bagheri & Komsa, *Scientific Data* (2023).
Pas de téléchargement en masse documenté sur la page — à creuser matériau par matériau ou via
le repo GitHub si besoin d'un accès programmatique.

### Materials Cloud — Archive 2024.148 ★ (le plus directement exploitable)

[Li, Gao, Xie et al., *High-throughput computation of ab initio Raman spectra for
two-dimensional materials*](https://doi.org/10.24435/materialscloud:bq-vp), Materials Cloud
Archive, 2024. **3 504 matériaux 2D**, spectres Raman calculés en DFPT all-electron
(code FHI-aims) — **presque 5× plus large que C2DB** (733 matériaux, trouvé en v0.1). CC BY
4.0, 4,2 Mo seulement pour tout le dataset.

**Téléchargé et inspecté concrètement** (voir [data/raw/materials_cloud_2024.148/](../data/raw/materials_cloud_2024.148/)
dans ce dépôt, qui contient un sous-ensemble curé de 14 matériaux correspondant exactement à
ceux du sujet — C, BN, MoS₂, WS₂, MoSe₂, WSe₂, plusieurs polymorphes chacun) :
- Format par matériau : `geometry.in` (structure FHI-aims), `POSCAR` (structure VASP),
  `raman.dat` (2 colonnes : fréquence en cm⁻¹, intensité en Å⁴/amu).
- Vérification physique faite sur `2192_MoS2` (1 Mo + 2 S = 3 atomes) : `raman.dat` contient
  exactement 9 lignes = 3N modes, ce qui confirme très concrètement la règle "maille de N
  atomes → 3N modes" du guide Raman (Question 28).
- Attention : le dossier `1849_C` a 8 atomes de carbone avec des coordonnées z différentes —
  ce n'est **pas** une monocouche de graphène simple. Il faudra trier les polymorphes
  (monocouche vs bicouche vs graphite, phase H vs T pour les TMDs) avant utilisation — détaillé
  dans le README du dossier de données.
- **Mise à jour (même jour)** : polymorphes triés avec `src/explore_materials_cloud_sample.py`
  (compte d'atomes + clustering des coordonnées z) — `577_C` et `1_BN` sont bien des
  monocouches simples (2 atomes), les paires MoS₂/WS₂/MoSe₂/WSe₂ donnent chacune une
  monocouche (3 atomes) et une bicouche (6 atomes) propres. Détail complet et CSV dans
  `data/raw/materials_cloud_2024.148/README.md`.
- **Découverte importante** : le spectre calculé du graphène monocouche ne montre **qu'un
  seul pic fort (~1443 cm⁻¹, le mode de type G)** — ni bande D, ni bande 2D. C'est attendu :
  ce sont des calculs **au point Γ sur un cristal parfait**, donc aucune bande activée par le
  désordre (D) ni aucun processus du second ordre (2D, qui implique des phonons hors Γ). **Ce
  type de dataset ab initio convient à l'identification de matériau (item 3) mais ne suffit
  pas seul pour l'indicateur de qualité/défauts D/G/2D (item 6)** — il faudra des données
  expérimentales ou des calculs dédiés sur des structures défectueuses pour ce dernier point.
- Comparaison chiffrée DFT vs expérience (voir README du dossier de données pour le détail) :
  G du graphène ~1443 cm⁻¹ calculé vs ~1580 cm⁻¹ expérimental (Ferrari & Basko, 2013), A₁g du
  MoS₂ ~396,5 cm⁻¹ calculé vs ~403 cm⁻¹ expérimental (Lee et al., 2010) — décalage systématique
  d'environ 1 à 9% vers le bas, effet DFT harmonique connu, à garder en tête si ce dataset sert
  à l'entraînement (risque de mauvaise généralisation sur données réelles sans recalibration).

→ **C'est la meilleure source "ab initio" trouvée jusqu'ici pour ce projet** : plus large que
C2DB, format plus simple (texte brut à 2 colonnes), et couvre exactement les matériaux visés
par le sujet avec plusieurs variantes par formule.

### Zenodo 17311728 — donnée expérimentale complémentaire

[*Twisted MoS₂ Bilayers as Functional Elements in Memtransistors*](https://zenodo.org/records/17311728)
— données Raman + photoluminescence **réelles** (pas calculées) sur MoS₂ monocouche, bicouche
2H et bicouche torsadée (twisted), sous contrainte électrique, avec données brutes et traitées,
notebooks de traitement mentionnés (non liés directement sur la page). CC BY 4.0, 21,3 Mo.
Utile comme **deuxième source expérimentale réelle** en plus des 594 spectres Qi et al. déjà
identifiés, mais le sujet de l'étude (effet du twist angle et de la tension électrique) est
différent de notre besoin (identification matériau + qualité) — à utiliser pour des spectres
MoS₂ "propres" de référence plutôt que pour l'indicateur de défauts.

### Lien arXiv fourni, non exploré

Le lien `arxiv.org/login?next_page=/submit/3160521/start` pointe vers une page de connexion
pour une **soumission arXiv privée** (brouillon en cours, identifiant 3160521) — ça nécessite
de se connecter à un compte personnel, donc je n'ai pas essayé d'y accéder (page privée, pas
une publication publique). Si ce lien devait pointer vers un article ou un dataset précis,
peux-tu redonner le lien final (après connexion) ou le DOI/arXiv ID une fois soumis ?

## 10. Sources — v0.1

- [A library of ab initio Raman spectra for automated identification of 2D materials (Nature Comms, 2020)](https://www.nature.com/articles/s41467-020-16529-6)
- [Deep Learning Assisted Raman Spectroscopy for Rapid Identification of 2D Materials (arXiv:2312.01389)](https://arxiv.org/pdf/2312.01389)
- [Raman and photoluminescence of MoS2 flakes and pyramids (Zenodo)](https://zenodo.org/records/5866629)
- [RamanBench: A Large-Scale Benchmark for Machine Learning on Raman Spectroscopy](https://www.researchgate.net/publication/404426482_RamanBench_A_Large-Scale_Benchmark_for_Machine_Learning_on_Raman_Spectroscopy)
- [Revisiting the Raman disorder band in graphene-based materials: A critical review (2025)](https://www.sciencedirect.com/science/article/pii/S0924203125000487)
- [RamanSPy: An open-source Python package for integrative Raman spectroscopy data analysis](https://pubs.acs.org/doi/10.1021/acs.analchem.4c00383)
- [RamPy (GitHub)](https://github.com/charlesll/rampy)
- [Recent Advances in Raman Spectral Classification with Machine Learning (MDPI Sensors)](https://www.mdpi.com/1424-8220/26/1/341)
- [Deep Learning for Raman Spectroscopy: A Review (MDPI)](https://www.mdpi.com/2673-4532/3/3/20)
- [Benchmarking deep learning models for Raman spectroscopy across open-source datasets (RSC Digital Discovery)](https://pubs.rsc.org/dd/article/5/8/3314/1277710/Benchmarking-deep-learning-models-for-Raman)
