# Q2. Conduct a chi-square goodness of fit test to determine if the distribution of colors of M&Ms in a bag
# matches the expected distribution of 20% blue, 20% orange, 20% green, 10% yellow, 10% red, and 20%
# brown. Use Python to perform the test with a significance level of 0.05.
import scipy.stats as stat

observed_data = [20,10,30,20,10,10]
expected_data = [20,20,20,10,10,20]

chisquare_test_statistics,p_value = stat.chisquare(observed_data,expected_data)
print(chisquare_test_statistics)
print(p_value)

significance_value = 0.05
dof = len(expected_data)- 1
print(dof)
critical_value = stat.chi2.ppf(1-significance_value,dof)
print(critical_value)


if chisquare_test_statistics > critical_value:
    print("Reject the Null Hypothesis")
else:
    print("Accept the Null hypothesis")