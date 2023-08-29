# Q5. Calculate the 90% confidence interval for a sample of data with a mean of 75 and a standard deviation
# of 12 using Python. Interpret the results.

sample_mean = 75 
std = 12

confidence_interval = 90
sample_size = 30 # assume 

z_value = 1.645

upper_bound = sample_mean + (z_value * std/(sample_mean**0.5))
print(upper_bound)

lower_bound = sample_mean - (z_value * std/(sample_mean**0.5))
print(lower_bound)

print("90% Confidence Interval:", (lower_bound, upper_bound))