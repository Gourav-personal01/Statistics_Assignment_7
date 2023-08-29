# Q8. A researcher hypothesizes that a coin is biased towards tails. They flip the coin 100 times and observe
# 45 tails. Conduct a chi-square goodness of fit test to determine if the observed frequencies match the
# expected frequencies of a fair coin. Use a significance level of 0.05.

import scipy.stats as stat
import numpy as np

# Null Hypothesis Ho - The coin is fair

# Alternate Hypothesis H1 - The coin is not fair


# Observed frequencies
observed = np.array([45, 100 - 45])  # Tails, Heads

# Expected frequencies for a fair coin (50-50)
expected = np.array([50, 50])

# Perform the chi-square goodness of fit test
chi2_statistic, p_value = stat.chisquare(observed, expected)

print("Chi-square statistic:", chi2_statistic)
print("P-value:", p_value)

if chi2_statistic > p_value :
    print("Reject the Null Hypothesis")
else:
    print("Accept the Null Hypothesis")