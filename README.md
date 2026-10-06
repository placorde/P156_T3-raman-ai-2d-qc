# P156_T3 — AI-Assisted Raman Analysis for 2D Electronic Device Quality Control

Projet d'Innovation Industrielle 4 & 5 (ESILV) — Projet n°156, équipe **P156_T3**.

Encadrante / partenaire projet : Sabrine Ayari (ESILV).

## Objectif

Développer une plateforme IA pour l'analyse automatisée de spectres Raman de matériaux 2D
(graphène, graphite, h-BN, TMDs : MoS₂, WS₂, MoSe₂, WSe₂), depuis la collecte de données
ouvertes jusqu'à un démonstrateur de prédiction, afin d'évaluer rapidement l'identité, la
structure et la qualité de ces matériaux avant leur intégration dans des dispositifs
électroniques (capteurs, transistors, photodétecteurs, électronique flexible).

Voir [docs/sujet_projet.md](docs/sujet_projet.md) pour l'énoncé complet,
[docs/cahier_des_charges.md](docs/cahier_des_charges.md) pour le document de cadrage, et
[docs/literature_review.md](docs/literature_review.md) pour la revue de littérature initiale
(physique Raman, jeux de données, état de l'art ML/DL).

## Contenu du projet

1. Prétraitement spectral : normalisation, correction de ligne de base, réduction de bruit,
   interpolation sur une grille spectrale commune.
2. Détection automatique des pics Raman et extraction de features physiques (position,
   largeur, intensité, ratios d'intensité).
3. Classification des matériaux 2D individuels et par familles (graphène/graphite, h-BN, TMDs).
4. Comparaison de modèles ML/DL (KNN, SVM, Random Forest, réseaux de neurones, CNN 1D).
5. Évaluation de la robustesse (bruit, décalages spectraux, variations d'intensité).
6. Indicateur de qualité spectrale pour les matériaux carbonés (bandes D, G, 2D).

## Livrables attendus

- Pipeline Python reproductible (prétraitement → features → ML → évaluation).
- Étude comparative des modèles (erreurs, robustesse, interprétabilité).
- Application web : upload d'un spectre, visualisation du signal traité et des pics détectés,
  prédiction du matériau / de la famille, indicateur de qualité.
- Ce dépôt : code, documentation, instructions d'installation, spectres d'exemple, licence
  open-source.
- Rapport scientifique et soutenance orale finale.

## Structure du dépôt

```
docs/           cahier des charges, sujet, notes de réunion
data/raw/       spectres bruts (open data)
data/processed/ spectres prétraités
notebooks/      exploration, prototypage
src/            pipeline (preprocessing, features, modèles, évaluation)
app/            application web (démonstrateur)
```

## Équipe — P156_T3

| Nom | Rôle |
|---|---|
| Pierre-Louis Lacorde | à compléter |
| ... | ... |

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

## Licence

Ce projet est distribué sous licence MIT (voir [LICENSE](LICENSE)), conformément à l'exigence
du sujet d'un dépôt open-source réutilisable.
