# Zenodo 5866629 — Raman et photoluminescence de flocons et pyramides de MoS₂

Source : [Raman and photoluminescence of MoS2 flakes and pyramids](https://zenodo.org/records/5866629),
DOI [10.5281/zenodo.5866629](https://doi.org/10.5281/zenodo.5866629), CC BY 4.0.

**Pourquoi ce dataset est important** : contrairement à `materials_cloud_2024.148/` (positions
de pics calculées, quelques valeurs discrètes), ce sont ici de **vrais spectres expérimentaux
continus** — exactement le type de données bruitées, avec fond de fluorescence et bruit
instrumental, sur lesquelles le pipeline de prétraitement du projet (item 1 du sujet :
normalisation, correction de ligne de base, réduction de bruit) devra être testé plus tard.

## Fichiers

- `MoS2-ML-Raman.txt` : spectre Raman d'un flocon de MoS₂ **monocouche** (ML = monolayer).
- `MoS2-pyramid-Raman.txt` : spectre Raman d'une **pyramide** de MoS₂ (structure 3D plus
  épaisse, probablement multicouche/massive au niveau de la pointe).
- Format : texte brut, 2 colonnes séparées par tabulation, **sans en-tête** — colonne 1 =
  décalage Raman (cm⁻¹, de ~51 à ~1828 cm⁻¹, pas d'environ 1,56 cm⁻¹, 1014 points), colonne 2 =
  intensité (unités arbitraires, pas précisées sur la page Zenodo).
- Les fichiers de photoluminescence (`MoS-ML-PL.txt`, `MoS-pyramid-PL.txt`) et l'image
  optique (`optical_MoS2_pyramid_on_Al2O3.tif`) existent sur Zenodo mais ne sont **pas**
  inclus ici (hors scope Raman pour l'instant) — à retélécharger depuis le DOI si besoin.

## Ce qu'on observe en traçant les spectres (2026-11-17)

Voir [`data/processed/zenodo_5866629_plots/`](../../processed/zenodo_5866629_plots/).

- **Deux pics nets vers 384 et 404 cm⁻¹** sur le flocon monocouche → correspond très
  précisément aux modes **E¹₂g** (~384,5 cm⁻¹) et **A₁g** (~403 cm⁻¹) attendus pour une
  monocouche de MoS₂ (Lee et al., 2010 — voir `docs/raman_guide`, Figure 4). Écart entre les
  deux pics ≈ 20 cm⁻¹, cohérent avec la valeur attendue pour une monocouche (~19 cm⁻¹).
- Sur la **pyramide**, les deux mêmes pics sont présents mais **plus écartés** (~384 et
  ~406 cm⁻¹) — cohérent avec une structure plus épaisse (l'écart E¹₂g/A₁g s'élargit avec le
  nombre de couches, cf. Question 46-47 du guide Raman).
- **Un pic très intense et net vers 520 cm⁻¹** apparaît sur le spectre complet (visible surtout
  sur le flocon monocouche, où le signal MoS₂ est plus faible en comparaison) : c'est
  presque certainement le **pic du substrat de silicium**, exactement l'exemple donné en
  Question 50 du guide Raman ("le pic très fin du silicium à 520 cm⁻¹... sert même couramment
  de référence de calibration"). **Première vraie illustration, sur nos propres données, de
  la distinction pic matériau / pic substrat.** À confirmer/exclure explicitement lors du
  prétraitement (ne pas le compter comme un pic du matériau).
- Fond de fluorescence visible (légère pente, bruit basse fréquence sur tout le spectre) —
  exactement ce que la correction de ligne de base du pipeline devra retirer.

## Prochaine étape (plus tard, pas maintenant)

Ce dataset est un bon candidat de test pour le futur pipeline de prétraitement
(`RamanSPy`) : il a à la fois des pics nets (MoS₂), un pic de substrat à exclure (Si à
520 cm⁻¹), du bruit et un fond de fluorescence — un cas d'usage complet en une seule paire de
fichiers.
