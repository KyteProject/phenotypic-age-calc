# Phenotypic Age Calculator

This repository contains a Python script designed to calculate an individual's phenotypic age based on various health biomarkers. This calculation is based on the algorithm developed by Dr. Levine, integrating comprehensive biomarker data to provide an insightful measure of biological aging.

## Overview

The script calculates phenotypic age using inputs from a set of specific biomarkers and the individual's chronological age. The calculation involves formulas derived from extensive research in the field of gerontology.

## Prerequisites

- Python 3.x
- NumPy library

Ensure that Python and NumPy are installed on your system to run the script successfully.

## Usage

1. **Input Biomarker Values**: Enter the values of the biomarkers as per your blood test results. These include Albumin, Creatinine, Glucose, C-reactive protein (CRP), Lymphocyte percent, Mean cell volume (MCV), Red cell distribution width (RDW), Alkaline phosphatase, and White blood cell count.

2. **Input Chronological Age**: Provide your chronological age in years.

3. **Run the Script**: Execute the script to calculate your phenotypic age.

## Biomarkers and Units

The script expects the following biomarkers with their respective units:

- Albumin (g/L)
- Creatinine (mmol/L)
- Glucose (mmol/L)
- C-reactive protein (CRP) (mg/dL)
- Lymphocyte percent (%)
- Mean cell volume (MCV) (fL)
- Red cell distribution width (RDW) (%)
- Alkaline phosphatase (IU/L)
- White blood cell count (x10^3 cells/µL)

Note: The script includes conversions for units that differ from the standard input.

## Script Details

The script `phenotypic_age_calculator.py` includes detailed comments explaining each part of the calculation. It first defines the constants and input values, handles unit conversions, applies the formula, and then outputs the estimated phenotypic age.

## Contributing

Contributions to improve the script or suggestions for further development are welcome. Please feel free to submit pull requests or open issues for discussion.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

This project is inspired by the research work of Dr. Levine and others in the field of biological aging. The original research papers and studies can be found in the references section of the accompanying blog article.

## References

- [My Blog Article](https://omux.dev/posts/calculating-phenotypic-age-with-python/)

- Liu Z, Kuo P-L, Horvath S, Crimmins E, Ferrucci L, Levine M (2019) **Correction: A new aging measure captures morbidity and
mortality risk across diverse subpopulations from NHANES IV: A cohort study. PLoS Med 16(2): e1002760.**
[https://doi.org/10.1371/iournal.pmed.1002760](https://doi.org/10.1371/iournal.pmed.1002760)

- Liu Z, Kuo PL, Horvath S, Crimmins E, Ferrucci L, et al. (2018) A new **aging measure captures morbidity and mortality risk across
diverse subpopulations from NHANES IV: A cohort study. PLOS Medicine 15(12): e1002718.**
[https://doi.org/10.1371/iournal.pmed.1002718](https://doi.org/10.1371/iournal.pmed.1002718)

- Levine ME, Lu AT, Quach A, Chen BH, Assimes TL, Bandinelli S, Hou L, **Baccarelli AA, Stewart JD, Li Y, Whitsel EA, Wilson JG, Reiner
AP, et al. An epigenetic biomarker of aging for lifespan and healthspan. Aging (Albany NY). 2018 Apr 1810:573-591.**
[https://doi.org/10.18632/aging.101414](https://doi.org/10.18632/aging.101414)

- [Online LATEX Equation Editor](https://latexeditor.lagrida.com)

- [Morgan Levine: ‘Only 10-30% of our lifespan is estimated to be due to genetics’ - The Guardian](https://www.theguardian.com/science/2022/may/07/morgan-levine-only-10-30-of-our-lifespan-is-estimated-to-be-due-to-genetics)