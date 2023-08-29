# Q7. A random sample of 1000 people was asked if they preferred Coke or Pepsi. Of the sample, 520
# preferred Coke. Calculate a 99% confidence interval for the true proportion of people in the population who
# prefer Coke.

import math
sample_size = 1000
sample_proportion = 0.512

confidence_interval = 90

z_value = 2.575

# confidence_interval = sample proportion +- (z*standard error ) 

lower_bound = sample_proportion - (z_value * math.sqrt((sample_proportion * (1 - sample_proportion)) / sample_size))
print(lower_bound)


upper_bound = sample_proportion + (z_value * math.sqrt((sample_proportion * (1 - sample_proportion)) / sample_size))
print(upper_bound)

print("95% Confidence Interval:", (lower_bound, upper_bound))