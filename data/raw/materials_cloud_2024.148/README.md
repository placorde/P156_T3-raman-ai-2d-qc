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

## Identification des polymorphes (faite le 2026-11-17 avec `src/explore_materials_cloud_sample.py`)

Script exécuté sur les 14 dossiers : lecture du `POSCAR` (nombre d'atomes, longueur de l'axe
c, clustering des coordonnées z pour détecter le nombre de plans atomiques distincts) +
lecture du `raman.dat` (modes acoustiques proches de 0 cm⁻¹ filtrés). Résultat complet dans
[`data/processed/materials_cloud_2024.148_summary.csv`](../../processed/materials_cloud_2024.148_summary.csv)
et un graphe par matériau dans
[`data/processed/materials_cloud_2024.148_plots/`](../../processed/materials_cloud_2024.148_plots/).

| Dossier | Atomes | Interprétation |
|---|---|---|
| `577_C` | 2 | **Graphène monocouche** (confirmé : 2 atomes de C, 1 seul plan z) |
| `543_C`, `1849_C` | 8 | Bicouche (ou super-cellule), **pas** une monocouche — 2 plans z détectés |
| `1_BN` | 2 | **h-BN monocouche** (même structure que le graphène monocouche) |
| `83_BN` | 8 | Super-cellule plane de h-BN (1 seul plan z malgré 8 atomes — probablement une
  cellule 2×2 d'une monocouche, intéressant comme base pour simuler des **défauts**, cf. item 6 du sujet) |
| `3278_BN` | 4 | Structure à 3 plans z — à vérifier plus en détail, pas une monocouche simple |
| `2192_MoS2`, `168_MoSe2`, `1348_WS2`, `291_WSe2` | 3 | **Monocouche TMD** (1 métal + 2 chalcogènes = le "sandwich" X-M-X d'une seule couche ; les "3 plans z" détectés sont les 3 plans de l'empilement S-Mo-S *dans la même monocouche*, pas 3 couches empilées) |
| `3103_MoS2`, `2398_MoSe2`, `2884_WS2`, `2453_WSe2` | 6 | **Bicouche TMD** (exactement le double — 2 métaux + 4 chalcogènes) |

→ Pour les TMDs, chaque paire (3 atomes / 6 atomes) donne directement monocouche / bicouche —
propre et exploitable tel quel. Pour C et BN, seuls `577_C` et `1_BN` sont des monocouches
simples ; les autres dossiers sont des structures plus complexes à ne pas utiliser comme
"graphène" ou "h-BN" de référence sans vérification supplémentaire.

## Découverte importante pour l'item 6 du sujet (indicateur de défauts)

En traçant `577_C` (graphène monocouche), **un seul pic Raman fort apparaît (~1443 cm⁻¹)** —
pas de bande D, pas de bande 2D. C'est normal et attendu, pas une erreur : ce dataset calcule
les modes **au point Γ** (centre de la zone de Brillouin) d'un cristal **parfait**. Or :
- la bande **D** n'existe que si le cristal a un défaut (elle est "activée par le désordre",
  cf. Question 20-21 du guide Raman) — ces structures sont des cristaux parfaits, donc pas de
  bande D ;
- la bande **2D** est un processus Raman du **second ordre** impliquant des phonons loin du
  point Γ (double résonance) — un calcul DFPT standard au point Γ ne la capture pas.

**Conséquence concrète pour le projet** : ce dataset (et plus généralement les bases "ab
initio Γ-point" comme C2DB) est excellent pour l'**identification de matériau** (item 3) mais
**ne suffit pas seul** pour l'indicateur de qualité/défauts basé sur D/G/2D (item 6) — il
faudra soit des données expérimentales réelles (qui ont ces bandes), soit des calculs dédiés
sur des super-cellules avec défauts (voir la piste `83_BN`, super-cellule plane, et le papier
Malenfant-Thuot et al. 2025 cité dans `docs/literature_review.md` §11, qui simule justement du
h-BN défectueux).

## Comparaison DFT ↔ expérience (premier repère chiffré)

| Matériau | Mode | Position calculée ici | Position expérimentale connue | Écart |
|---|---|---|---|---|
| Graphène monocouche (`577_C`) | G | ~1443 cm⁻¹ | ~1580 cm⁻¹ (Ferrari & Basko, 2013) | ~−9% |
| MoS₂ monocouche (`2192_MoS2`) | A₁g | ~396,5 cm⁻¹ | ~403 cm⁻¹ (Lee et al., 2010) | ~−1,6% |
| MoS₂ monocouche (`2192_MoS2`) | E¹₂g | ~362 cm⁻¹ (pic le plus proche) | ~384,5 cm⁻¹ (Lee et al., 2010) | ~−6% |

Le décalage systématique vers le bas est un effet DFT connu (pas d'anharmonicité/température
incluse dans un calcul harmonique standard) — **à mentionner explicitement dans le rapport**
si ce dataset sert à l'entraînement : un modèle entraîné uniquement sur ces positions
calculées risque de mal généraliser sur des spectres expérimentaux sans recalibration.

## Ce qu'il reste à faire avec ces données

1. ~~Identifier précisément quel dossier correspond à quelle structure exacte~~ → fait
   ci-dessus pour les 14 exemples ; à refaire si on élargit au dataset complet (3 504
   matériaux).
2. Décider comment gérer l'écart DFT/expérience ci-dessus (recalibration simple par décalage
   constant ? entraînement mixte simulé+réel ? à trancher avec la partenaire).
3. Pour l'indicateur qualité (item 6), chercher/générer des spectres avec défauts réels
   (expérimentaux, ou super-cellules dédiées) plutôt que de compter sur ce dataset seul.
4. Comparer un spectre calculé ici à un spectre expérimental complet (ex. Figure 4 du guide
   Raman, Lee et al. 2010) sur toute la gamme, pas juste les positions de pics.
