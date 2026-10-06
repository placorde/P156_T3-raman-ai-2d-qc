# Sujet — Projet n°156

> Copie de référence de l'énoncé officiel (PDF fourni par l'école). Ne pas modifier ce fichier :
> toute reformulation / interprétation va dans `cahier_des_charges.md`.

**Titre :** AI-Assisted Raman Analysis for 2D Electronic Device Quality Control.

## I. Project description

Two-dimensional (2D) materials, including graphene, graphite, hexagonal boron nitride (h-BN),
and transition metal dichalcogenides (TMDs: MoS₂, WS₂, MoSe₂ and WSe₂), are central to a range
of emerging technologies. Their electrical, optical, thermal and mechanical properties make
them promising candidates for smart and wearable sensors, flexible electronics, photodetectors,
optoelectronic devices, energy-storage systems, and structural or industrial-process monitoring.

However, moving these materials from laboratory research to reliable and reproducible devices
requires fast control of their identity, structure and quality. Misidentification, phase variations,
degradation or defects can strongly affect the performance of a sensor, transistor or electronic
component. Raman spectroscopy is a particularly relevant non-destructive technique for this
purpose because it provides a specific vibrational signature for each material.

The aim of this project is to develop an IA platform for the automated analysis of Raman spectra
from 2D materials. You will build a complete workflow, from open-data collection to a prediction
demonstrator. This project addresses an important engineering challenge: ensuring that 2D
materials are suitable before they are integrated into devices. Graphene and TMDs are
promising for transistors, sensors, photodetectors and flexible electronics. Their performance
depends strongly on material quality, crystal structure and defect level. Raman spectroscopy can
assess these properties without damaging the sample, but its interpretation requires expertise.
The proposed AI tool will automate this analysis and provide rapid material identification and
quality assessment. It could help engineers select reliable materials and detect unsuitable
samples early in the development or manufacturing process.

The project will include:

1. Spectral preprocessing: normalisation, baseline correction, noise reduction and interpolation
   onto a common spectral grid.
2. Automated Raman peak detection and extraction of physically meaningful features, including
   peak positions, widths, intensities and intensity ratios.
3. Classification of individual 2D materials and material families, such as graphene/graphite,
   h-BN and TMDs.
4. Comparison of machine-learning and deep-learning models, including KNN, SVM, Random
   Forest, neural networks and 1D CNNs.
5. Robustness assessment under noise, spectral shifts and intensity variations, which are
   realistic conditions in industrial measurements.
6. Development of a spectral-quality indicator for carbon-based materials. The D, G and 2D
   Raman bands of graphene or graphite will be analysed to identify spectral disorder or probable
   defects.

## II. Expected deliverables

1. A reproducible Python project containing the complete data-processing, feature-extraction,
   machine-learning and evaluation pipeline.
2. A comparative performance study of the selected models, including error analysis, robustness
   tests and model-interpretability results.
3. A functional web application with a user-friendly interface. The user will be able to upload a
   Raman spectrum, visualise the processed signal and detected peaks, and obtain the predicted
   material, material family and, where relevant, a spectral-quality or defect indicator.
4. A public open-source code repository, containing the program, documentation, installation
   instructions, example spectra and the application source code. The repository should use an
   open-source licence and enable another user to reproduce and run the project.
5. A scientific report and a final oral presentation.

The final objective is to deliver an open, reproducible and usable engineering tool that
transforms Raman spectra into automated decisions for the identification and quality
assessment of advanced 2D materials.

## Informations sur le projet

- **Compétences développées :** Analyse de données scientifiques ; traitement du signal et
  prétraitement de spectres Raman ; extraction et visualisation de caractéristiques spectrales ;
  machine learning et deep learning (SVM, Random Forest, CNN 1D) ; évaluation et interprétation
  de modèles ; développement d'une application web ; gestion de données et code open source ;
  rédaction scientifique et présentation technique.
- **Prérequis :** bases en programmation Python (NumPy, Pandas, Matplotlib), IA et notions
  élémentaires de machine learning.
- **Majeure(s) concernée(s) :** EVD, MDS, DIA, CCC, EVD_Alt, MDS_Alt, DIA_Alt, CCC_Alt, MMN,
  MMN_Alt
- **Année(s) concernée(s) :** A4, A5 (acceptera une équipe A4 si aucune équipe A5 ne se positionne)
- **Mots-clés :** Data Science, IA, Machine learning, Modélisation, Programmation, Python,
  Simulation, Traitement de donnée, Web

## Partenaire

- **École :** ESILV
- **Référente projet :** Sabrine Ayari
