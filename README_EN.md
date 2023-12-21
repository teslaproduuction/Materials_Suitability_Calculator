# Materials Suitability Calculator

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/teslaproduuction/Materials_Suitability_Calculator/blob/master/README_EN.md)
[![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](https://github.com/teslaproduuction/Materials_Suitability_Calculator/blob/master/README.md)

## Project Description

This repository contains the source code and materials related to the study of the thermal resistance of materials used for dies and molds in pressure die casting. The project involves a comparison of theoretical criteria for thermal resistance based on the mechanical and thermophysical properties of various steels. The analysis is conducted using rank correlation between the calculated and experimental assessments of steel's thermal resistance.

## Key Features

- **Comparative Analysis of Material Properties:** The study includes an analysis of thermophysical and mechanical properties of steels, such as tensile strength, yield strength, elongation, hardness, and others.

- **Rank Correlation:** The method of rank correlation analysis is applied to assess the relationship between theoretical and experimental data on thermal resistance.

- **Determination of Optimal Steel Grade:** The project tackles the challenging task of choosing the optimal steel grade for hot bulk forming dies and pressure die casting molds, taking into account operational and economic aspects.

## How to Use

**Downloading the Compiled Version:**

In addition to the option of using the application's source code directly from the repository, we provide the option to download a ready-to-use, compiled version of the application. This allows users unfamiliar with the Python application compilation process to quickly obtain and use the application on their devices.

To download the compiled version of the application, follow these steps:

1. Go to the "Releases" page in the GitHub repository or use the following [релиз](https://github.com/teslaproduuction/Materials_Suitability_Calculator/releases).

2. Find the latest release where the compiled version of the application is available.

3. In the "Assets" section, find and download the file with the extension corresponding to your operating system (e.g., .exe for Windows, .app for macOS (coming soon), or .tar.gz for Linux).

4. After the download is complete, install or run the application according to the instructions for your operating system.

## Formulas

| № | Критерий | № | Критерий |
|---|----------|---|----------|
| 1 | $K_{1}=\lambda \cdot \sigma_{B} / \alpha \cdot E$ | 9 | $K_{9}=\sigma_{0,2} / \tau \cdot \alpha$ |
| 2 | $K_{2}=\lambda \cdot \delta / \alpha \cdot E$ | 10 | $K_{10}=\sigma_{t . \max } / \sigma_{0,2}$ |
| 3 | $K_{3}=\lambda \cdot K C U / \alpha \cdot E$ | 11 | $K_{11}=\frac{\delta}{2\left[\alpha \cdot \Delta t /(1-\mu)-\left(2 \sigma_{0,2} / E\right)\right]}$ |
| 4 | $K_{4}=\lambda / \alpha \cdot c \cdot \rho$ | 12 | $K_{12}=\frac{K C U}{\sigma_{0,2} \cdot\left(\alpha \cdot t_{\kappa}-2 \sigma_{0,2} / E\right)}$ |
| 5 | $K_{5}=a / \alpha \cdot E$ | 13 | $K_{13}=\frac{\sigma_{B} \cdot \psi}{\sigma_{0,2} \cdot\left(1-\psi^{2}\right) \alpha \cdot \Delta t}$ |
| 6 | $K_{6}=\sigma_{B} \cdot(1-\mu) / \alpha \cdot E$ | 14 | $K_{14}=\left[\frac{\sigma_{B} \cdot(1+\delta+\psi)-\sigma_{0,2}}{E \cdot(\alpha \cdot \Delta t)^{2}}\right.$ |
| 7 | $K_{7}=a \cdot \sigma_{B} \cdot(1-\mu) / \alpha \cdot E$ | 15 | $K_{15}=\left(\frac{\sigma_{B}-\alpha \cdot \Delta t \cdot E / 1-\mu}{\frac{\sigma_{0,2}}{E}+\frac{\alpha \cdot \Delta t}{1-\mu} \cdot \frac{\alpha \cdot \Delta t \cdot E}{1-\mu}}\right)$ |
| 8 | $K_{8}=\sigma_{B} / H R C \cdot E$ | 16 | $K_{16}=\frac{\ln \frac{100}{100-\psi}}{2 \cdot \frac{\alpha \cdot \Delta t}{1-\mu}-4 \cdot \frac{\sigma_{0,2}}{E}}$ |
