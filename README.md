<h1 align="center">
AI-Assisted Dark Matter Halo Morphology Reconstruction Using SPARC Galaxy Rotation Curves
</h1>

<p align="center">
<b>Abhaya Kanwar</b><br>
Computer Science (Artificial Intelligence & Machine Learning)<br>
Jaypee University of Information Technology
</p>

<p align="center">
Dark Matter • Computational Astrophysics • Machine Learning • SPARC Database
</p>

<p align="center">
<img src="results/Rotation_curve.png" width="850">
</p>

---

## Overview

This project investigates galactic dark matter halo structures using observed galaxy rotation curve data from the SPARC database.

Four dark matter halo models are analyzed and compared:

- Isothermal Halo
- Burkert Halo
- Einasto Halo
- Navarro–Frenk–White (NFW) Halo

In addition to classical halo fitting, this work introduces an AI-assisted framework capable of classifying galaxies into cored, transitional, and cuspy dark matter halo morphologies using machine learning techniques.

---

## Research Objectives

- Compare cored and cuspy dark matter halo models.
- Investigate the core–cusp problem.
- Perform baryonic mass decomposition.
- Develop an AI-assisted halo morphology classifier.
- Explore hybrid dark matter halo structures.
- Apply machine learning to computational astrophysics.

---

## Key Results

| Metric | Value |
|----------|----------|
| Halo Models Compared | 4 |
| Dataset | SPARC Galaxy Rotation Curves |
| Classification Accuracy | 85.38% |
| Validation Method | 5-Fold Cross Validation |
| Best Halo Model | Burkert Halo |
| AI Framework | Ensemble Learning |
| Morphology Classes | Cored, Transitional, Cuspy |

---

# Results

## Rotation Curve Comparison

<p align="center">
<img src="results/Rotation_curve.png" width="750">
</p>

Comparison of observed galaxy rotation curves with Isothermal, Burkert, Einasto, and NFW dark matter halo models.

---

## Statistical Model Comparison

<p align="center">
<img src="results/Comparison.png" width="700">
</p>

Reduced χ², AIC, and BIC comparison of the four halo models.

---

## Residual Analysis

<p align="center">
<img src="results/Residual.png" width="700">
</p>

Residual distributions used to evaluate systematic fitting errors.

---

## Density Profile Comparison

<p align="center">
<img src="results/Density.png" width="700">
</p>

Comparison of dark matter density structures for the Isothermal, Burkert, Einasto, and NFW profiles.

---

## Hybrid Halo Model

<p align="center">
<img src="results/Hybrid_halo_model.png" width="750">
</p>

Phenomenological hybrid halo profile combining core-like and transitional dark matter behavior.

---

## Baryonic Decomposition

<p align="center">
<img src="results/baryonic_decomposition.png" width="750">
</p>

Contribution of stellar disk, gas, bulge, and dark matter halo to the total rotation curve.

---

## Confusion Matrix

<p align="center">
<img src="results/confusion_matrix.png" width="600">
</p>

Classification performance for cored, transitional, and cuspy halo morphologies.

---

## ROC Curve Analysis

<p align="center">
<img src="results/roc_curve.png" width="700">
</p>

Receiver Operating Characteristic curves demonstrating classifier performance.

---

## Learning Curve

<p align="center">
<img src="results/Learning_curve.png" width="700">
</p>

Training and validation accuracy as a function of dataset size.

---

## Feature Importance Analysis

<p align="center">
<img src="results/feature_importance.png" width="700">
</p>

Relative importance of rotation curve features used by the machine learning framework.

---

# Methodology

1. Acquire galaxy rotation curve data from the SPARC database.
2. Construct Isothermal, Burkert, Einasto, and NFW halo models.
3. Perform baryonic decomposition.
4. Fit halo parameters using chi-square minimization.
5. Evaluate model quality using χ², AIC, and BIC statistics.
6. Extract physically motivated rotation curve features.
7. Train ensemble machine learning classifiers.
8. Evaluate performance using cross-validation and ROC/AUC metrics.
9. Investigate hybrid halo structures.

---

# Repository Structure

```text
ai-darkmatter-halo-reconstruction/
│
├── paper/
│   └── research_paper.pdf
│
├── results/
│   ├── Comparison.png
│   ├── Density.png
│   ├── Hybrid_halo_model.png
│   ├── Learning_curve.png
│   ├── Residual.png
│   ├── Rotation_curve.png
│   ├── baryonic_decomposition.png
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── roc_curve.png
│
├── README.md
└── requirements.txt
```

---

# Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Scikit-Learn
- Machine Learning
- Computational Astrophysics
- Statistical Modeling

---

# Research Paper

The complete research paper is available in:

```text
paper/research_paper.pdf
```

---

# Citation

```text
Abhaya Kanwar.
AI-Assisted Dark Matter Halo Morphology Reconstruction Using SPARC Galaxy Rotation Curves.
2026.
```

---

# Author

**Abhaya Kanwar**

Computer Science (Artificial Intelligence & Machine Learning)

Jaypee University of Information Technology

### Research Interests

- Computational Astrophysics
- Artificial Intelligence
- Machine Learning for Science
- Dark Matter Physics
- Scientific Computing

---

 If you found this project interesting, consider starring the repository.
