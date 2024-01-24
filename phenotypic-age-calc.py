import numpy as np

# Given values from the spreadsheet
albumin = 4.1  # g/L - this may need converted from g/dL
creatinine = 0.73  # mmol/L - this may need converted from mg/dL
glucose = 94  # mmol/L - this may need converted from mg/dL
crp = 0.19  # mg/dl - this may need converted from mg/L
lymphocyte_percent = 27.78  # %
mcv = 88  # fL
rdw = 13.6  # %
alkaline_phosphatase = 48  # IU/L
white_blood_cell_count = 3.9  # x10^3 cells/µL
chronological_age = 64.12  # years

# Constants from the formula
b0 = -19.9067
b_albumin = -0.0336
b_creatinine = 0.0095
b_glucose = 0.1953
b_crp = 0.0954
b_lymphocyte_percent = -0.0120
b_mcv = 0.0268
b_rdw = 0.3306
b_alkaline_phosphatase = 0.00188
b_white_blood_cell_count = 0.0554
b_chronological_age = 0.0804

# xb calculation
xb = (
    b0
    + (b_albumin * (albumin * 10))
    + (b_creatinine * (creatinine * 88.401))
    + (b_glucose * (glucose * 0.0555))
    + (b_crp * np.log(crp * 0.1))
    + (b_lymphocyte_percent * lymphocyte_percent)
    + (b_mcv * mcv)
    + (b_rdw * rdw)
    + (b_alkaline_phosphatase * alkaline_phosphatase)
    + (b_white_blood_cell_count * white_blood_cell_count)
    + (b_chronological_age * chronological_age)
)

# M calculation
gamma = -1.51714
lambda_ = 0.0076927
M = 1 - np.exp((gamma * np.exp(xb)) / lambda_)

# Phenotypic Age calculation
alpha = 141.50225
beta = -0.00553
phenotypic_age = alpha + (np.log(beta * np.log(1 - M)) / 0.09165)

print(phenotypic_age)
