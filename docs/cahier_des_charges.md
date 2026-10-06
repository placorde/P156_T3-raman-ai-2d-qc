# Cahier des charges — Draft v0.1 (P156_T3)

> Document de travail à compléter en équipe avant le kick-off avec la partenaire (Sabrine
> Ayari), qui doit avoir lieu **avant le 09 octobre**. À réviser après l'échange avec elle.

## 1. Compréhension du projet et objectifs

Le projet consiste à construire une chaîne de traitement complète permettant d'analyser
automatiquement des spectres Raman de matériaux 2D (graphène, graphite, h-BN, TMDs : MoS₂,
WS₂, MoSe₂, WSe₂) pour :

- identifier le matériau et sa famille à partir de son spectre Raman ;
- évaluer sa qualité / son niveau de défauts (en particulier via les bandes D, G et 2D pour les
  matériaux carbonés) ;
- fournir cette analyse via une application web utilisable par un non-expert (upload d'un
  spectre → visualisation → prédiction).

L'enjeu métier : avant d'intégrer un matériau 2D dans un composant électronique (capteur,
transistor, photodétecteur...), il faut pouvoir vérifier rapidement et sans expertise Raman
poussée que l'échantillon est conforme — d'où l'intérêt d'un outil IA de diagnostic rapide.

Le livrable final attendu est un **outil d'ingénierie open, reproductible et utilisable**, pas
seulement une preuve de concept en notebook.

## 2. Besoins et attentes identifiés

- Un pipeline Python reproductible : acquisition de données ouvertes → prétraitement
  (normalisation, correction de ligne de base, débruitage, interpolation) → extraction de
  features (position/largeur/intensité des pics, ratios) → modèles ML/DL → évaluation.
- Une comparaison argumentée de plusieurs modèles (KNN, SVM, Random Forest, réseaux de
  neurones, CNN 1D), avec analyse d'erreurs, tests de robustesse (bruit, décalage spectral,
  variations d'intensité) et un minimum d'interprétabilité.
- Un indicateur de qualité spectrale pour les matériaux carbonés (désordre structurel /
  défauts probables via bandes D/G/2D).
- Une application web simple : upload d'un spectre, visualisation du signal traité et des pics
  détectés, prédiction du matériau/famille + indicateur de qualité si pertinent.
- Un dépôt GitHub public, sous licence open-source, documenté et installable par un tiers
  (ce dépôt).
- Un rapport scientifique et une soutenance orale finale.

## 3. Questions à clarifier avec la partenaire

- Quelles sources de données Raman ouvertes recommande-t-elle (bases publiques, publications
  avec spectres partagés, données internes ESILV/labo) ? Y a-t-il un jeu de données de
  référence déjà identifié ?
- Quel niveau de granularité est attendu pour la classification : matériau individuel
  (ex. MoS₂ vs WS₂) et/ou famille (TMD vs graphène/graphite vs h-BN) ?
- Comment est définie/mesurée la "qualité" ou le "défaut" attendu en sortie (ratio I(D)/I(G),
  largeur de bande, label qualitatif, score continu) ? Existe-t-il une vérité terrain
  (labels) disponible ?
- Quel niveau d'exigence sur la robustesse (bruit, décalage, variation d'intensité) : bruit
  synthétique ajouté par nous, ou données réelles bruitées fournies ?
- Contraintes/préférences techniques pour l'application web (stack imposée, hébergement,
  interface minimale vs plus poussée) ?
- Quel format de rendu attendu pour le rapport scientifique et la soutenance (gabarit, durée,
  jalons intermédiaires) ?
- Disponibilité de la partenaire pour des points d'avancement réguliers (fréquence,
  canal de communication) ?

## 4. Organisation de l'équipe (P156_T3)

| Nom | Rôle pressenti | Périmètre |
|---|---|---|
| Pierre-Louis Lacorde | à définir avec l'équipe | — |
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |

*(à compléter lors de la première réunion d'équipe — cf. section 5)*

Pistes de répartition par lot technique (à ajuster selon affinités) :

- **Data & prétraitement** : collecte des spectres open-data, normalisation, correction de
  ligne de base, détection de pics.
- **Modélisation ML/DL** : feature engineering, entraînement/comparaison KNN/SVM/RF/CNN 1D,
  évaluation et robustesse.
- **Indicateur qualité matériaux carbonés** : analyse bandes D/G/2D, définition du score.
- **Application web** : interface utilisateur, intégration du pipeline/modèle, déploiement.
- **Documentation & gestion de projet** : dépôt GitHub, README, rapport scientifique,
  coordination des jalons, interface avec la partenaire.

## 5. Premières étapes

1. Réunion d'équipe interne : lecture commune du sujet, répartition provisoire des rôles,
   création de ce dépôt (fait ✅), choix des outils (gestion de tâches, canal de
   communication).
2. Finaliser les questions de la section 3 et contacter la partenaire (Sabrine Ayari) dès
   réception de ses coordonnées par le référent d'équipe.
3. Organiser et tenir le kick-off avec la partenaire avant le **09/10**.
4. Mettre à jour ce document après le kick-off (réponses obtenues, périmètre affiné, rôles
   définitifs).
5. Démarrer la recherche de jeux de données Raman ouverts en parallèle, sans attendre le
   kick-off.

## 6. Historique des révisions

- v0.1 — brouillon initial généré à partir du sujet, avant tout échange avec la partenaire.
