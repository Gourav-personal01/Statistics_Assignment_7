# Q10. A study was conducted to determine if the proportion of people who prefer milk chocolate, dark
# chocolate, or white chocolate is different in the U.S. versus the U.K. A random sample of 500 people from
# the U.S. and a random sample of 500 people from the U.K. were surveyed. The results are shown in the
# contingency table below. Conduct a chi-square test for independence to determine if there is a significant
# association between chocolate preference and country of origin.

# Use a significance level of 0.01.

# Milk Chocolate

# U.S. (n=500) 200 150 150
# U.K. (n=500) 225 175 100

# Null Hypothesis - There is a significant change
# Alternate Hypotheis - There is no significant change

import scipy.stats as stat
import numpy as np

observed_value = np.array([[200, 150,150],
                     [225, 175,100]])

chi2, p, dof, expected = stat.chi2_contingency(observed_value)

print("Chi-square statistic:", chi2)
print("P-value:", p)
print(dof)
if chi2 > p :
    print("Reject the Null Hypothesis")
else:
    print("Accept the Null Hypothesis")