# Q1. Calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation
# of 5 using Python. Interpret the results.

sample_mean = 50
std = 5
confidence_interval = 0.95
critical_value = 1.95
sample_size = 10 # assume 

lower_confidence_interval = sample_mean - (critical_value * (std/(sample_size**0.5)))

higher_confidence_interval = sample_mean + (critical_value * (std/(sample_size**0.5)))

print(f"The population mean lies between {lower_confidence_interval} and {higher_confidence_interval} ")