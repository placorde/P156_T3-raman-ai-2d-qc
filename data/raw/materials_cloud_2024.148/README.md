# Sous-ensemble : Materials Cloud Archive 2024.148

Source : Li, Gao, Xie et al., *High-throughput computation of ab initio Raman spectra for
two-dimensional materials*, Materials Cloud Archive, record 2024.148 (2024),
DOI: [10.24435/materialscloud:bq-vp](https://doi.org/10.24435/materialscloud:bq-vp).
Licence CC BY 4.0. Dataset complet : 3 504 matériaux 2D (spectres Raman calculés en DFPT
all-electron, code FHI-aims).

Ce dossier contient uniquement un **sous-ensemble curé** (14 dossiers / 57 Ko) correspondant
aux matériaux explicitement cités dans le sujet du projet (plusieurs polymorphes/empilements
par formule quand le dataset en propose) :

| Formule | Dossiers inclus | Matériau visé |
|---|---|---|
| C | `1849_C`, `543_C`, `577_C` | Graphène / graphite (plusieurs empilements — à trier, voir note ci-dessous) |
| BN | `1_BN`, `3278_BN`, `83_BN` | h-BN |
| MoS2 | `2192_MoS2`, `3103_MoS2` | TMD |
| WS2 | `1348_WS2`, `2884_WS2` | TMD |
| MoSe2 | `168_MoSe2`, `2398_MoSe2` | TMD |
| WSe2 | `291_WSe2`, `2453_WSe2` | TMD |

Le dataset complet (3 504 matériaux, 4,2 Mo) peut être retéléchargé depuis le lien DOI
ci-dessus si besoin d'élargir au-delà de ces 14 exemples.

## Format de chaque dossier (`README_source.txt` original)

- `geometry.in` : fichier d'entrée FHI-aims (structure atomique).
- `POSCAR` : même structure, format VASP.
- `raman.dat` : résultat du calcul — **colonne 1** = fréquence du mode (cm⁻¹, décalage Raman),
  **colonne 2** = intensité Raman calculée (Å⁴/amu). Les premières lignes à fréquence proche
  de 0 et intensité quasi nulle sont les **modes acoustiques** (voir Question 29 du guide
  Raman : phonons acoustiques vs optiques) — ce ne sont pas des pics Raman réels, à filtrer
  avant tout entraînement.

## Vérifications faites en l'inspectant (2026-11-17)

- `2192_MoS2` a bien 1 Mo + 2 S (3 atomes) → `raman.dat` contient exactement 9 lignes = 3N
  modes (confirme la Question 28 du guide Raman : maille de N atomes → 3N modes).
- `1849_C` a 8 atomes de carbone dans la maille, avec des coordonnées z différentes par
  atome → ce n'est **pas** une monocouche de graphène simple (2 atomes), mais un empilement
  multicouche ou un polymorphe particulier. **À vérifier avant utilisation** : comparer les
  3 dossiers `C` entre eux (nombre d'atomes, coordonnées) pour identifier lequel est le
  graphène monocouche pur, lequel est bicouche/graphite, etc. Idem à vérifier pour les 3
  dossiers `BN` et les paires `MoS2`/`WS2`/`MoSe2`/`WSe2` (polymorphes H vs T, nombre de
  couches).

## Ce qu'il reste à faire avec ces données

1. Identifier précisément quel dossier correspond à quelle structure exacte (via `POSCAR` /
   nombre d'atomes / c-axis) plutôt que de supposer "C = graphène".
2. Écrire un petit script de chargement qui lit `raman.dat`, filtre les modes acoustiques
   proches de 0, et convertit vers le même format que les autres sources (594 spectres
   expérimentaux, Zenodo MoS₂) pour pouvoir les combiner dans `src/`.
3. Comparer un spectre calculé ici à un spectre expérimental connu (ex. Lee et al. 2010 pour
   MoS₂, voir `docs/raman_guide` / Figure 4) pour avoir une première idée de l'écart
   simulation/expérience.
