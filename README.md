# PyRo5

**An Automated Python Pipeline for High-Throughput Pre-Docking Ligand Screening**

[![DOI](https://img.shields.io/badge/DOI-10.13140%2FRG.2.2.28702.70721-blue)](https://doi.org/10.13140/RG.2.2.28702.70721)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview
PyRo5 is a Python-based chemoinformatics pipeline that leverages RDKit to programmatically evaluate drug candidates against **Lipinski's Rule of Five** and **Veber's Rules** prior to molecular docking. By rapidly computing molecular descriptors (MW, LogP, HBD, HBA, TPSA, Rotatable Bonds), PyRo5 filters out non-druglike compounds before they enter costly docking simulations.

## Features
- Calculates Lipinski's Rule of Five parameters
- Calculates Veber's Rules (TPSA, Rotatable Bonds)
- Generates 2D molecular structure visualizations via RDKit
- Clean, extensible Python codebase

## Installation
```bash
pip install rdkit
```

## Usage
```bash
python pyro5.py
```

## Example Output
```
--- Aspirin ---
MW: 180.16
LogP: 1.31
HBD: 1
HBA: 3
TPSA: 63.60
RotBonds: 2

--- Ibuprofen ---
MW: 206.28
LogP: 3.07
HBD: 1
HBA: 1
TPSA: 37.30
RotBonds: 4

--- Paclitaxel ---
MW: 809.91
LogP: 4.44
HBD: 4
HBA: 12
TPSA: 194.99
RotBonds: 9
```

## Citation
If you use this pipeline in your research, please cite:

> Rivera, K.A.T. (2026). *PyRo5: An Automated Python Pipeline for High-Throughput Pre-Docking Ligand Screening*. Preprint. DOI: [10.13140/RG.2.2.28702.70721](https://doi.org/10.13140/RG.2.2.28702.70721)

## Author
**Ken Alexander T. Rivera**
Mabalacat City College, Philippines
- [ResearchGate](https://www.researchgate.net/profile/Ken-Alexander-Rivera)
- [ORCID](https://orcid.org/0009-0006-2016-8507)
- [TalanaiHub](https://talanaihub.com)

## License
This project is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
