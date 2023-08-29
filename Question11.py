# Q11. A random sample of 30 people was selected from a population with an unknown mean and standard
# deviation. The sample mean was found to be 72 and the sample standard deviation was found to be 10.
# Conduct a hypothesis test to determine if the population mean is significantly different from 70. Use a
# significance level of 0.05.

sample_size = 30 
sample_mean = 72
sample_std = 10
population_mean = 70
confidence_interval = 95

z_value1 = 1.96
z_value2 = -1.96
# This is Two tail test
# Null Hypothesis Ho - there is significant change
# Alternate Hypothesis Ho - there is no significant change

z_score =  (population_mean - sample_mean)/(sample_std/(sample_size**0.5))
print(z_score)

if z_score > z_value1 or z_score < z_value2:
    print("We Reject the Null Hypothesis")
else:
    print("accept the null hypothesis")
