# Q4. A study of the prevalence of smoking in a population of 500 individuals found that 60 individuals
# smoked. Use Python to calculate the 95% confidence interval for the true proportion of individuals in the
# population who smoke.

import math
sample_size = 500 
sample_proportion = 0.12
z_value = 1.96

# confidence_interval = sample proportion +- (z*standard error ) 

lower_bound = sample_proportion - (z_value * math.sqrt((sample_proportion * (1 - sample_proportion)) / sample_size))
print(lower_bound)


upper_bound = sample_proportion + (z_value * math.sqrt((sample_proportion * (1 - sample_proportion)) / sample_size))
print(upper_bound)

print("95% Confidence Interval:", (lower_bound, upper_bound))