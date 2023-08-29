# Q3. Use Python to calculate the chi-square statistic and p-value for a contingency table with the following
# data:

# Outcome 1 20 15
# Outcome 2 10 25
# Outcome 3 15 20

# Interpret the results of the test.

import scipy.stats as stat
import numpy as np

observed_value = np.array([[20, 15],
                     [10, 25],
                     [15, 20]])

chi2, p, dof, expected = stat.chi2_contingency(observed_value)

print("Chi-square statistic:", chi2)
print("P-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies:\n", expected)
