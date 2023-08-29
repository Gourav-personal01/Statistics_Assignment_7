# Q9. A study was conducted to determine if there is an association between smoking status (smoker or
# non-smoker) and lung cancer diagnosis (yes or no). The results are shown in the contingency table below.
# Conduct a chi-square test for independence to determine if there is a significant association between
# smoking status and lung cancer diagnosis.

# Lung Cancer: Yes

# Smoker 60 140
# Non-smoker 30 170

# Use a significance level of 0.05.

# Null Hypothesis Ho - There is a significant change

# Alternate Hypothesis H1 - There is no significant change 


import scipy.stats as stat
import numpy as np

observed_value = np.array([[60, 140],
                     [30, 170]])

chi2, p, dof, expected = stat.chi2_contingency(observed_value)

print("Chi-square statistic:", chi2)
print("P-value:", p)
print(dof)
if chi2 > p :
    print("Reject the Null Hypothesis")
else:
    print("Accept the Null Hypothesis")