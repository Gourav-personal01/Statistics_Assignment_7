# Q6. Use Python to plot the chi-square distribution with 10 degrees of freedom. Label the axes and shade the
# area corresponding to a chi-square statistic

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Degrees of freedom
df = 10

# Create a range of x values for the plot
x = np.linspace(0, 30, 500)

# Calculate the chi-square probability density function (PDF) for the given degrees of freedom
pdf = chi2.pdf(x, df)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label=f'Chi-square (df={df})')

# Shade the area corresponding to a chi-square statistic
chi2_statistic = 15  # Change this to the desired chi-square statistic
x_shaded = np.linspace(0, chi2_statistic, 500)
pdf_shaded = chi2.pdf(x_shaded, df)
plt.fill_between(x_shaded, pdf_shaded, color='gray', alpha=0.3, label=f'Chi-square statistic = {chi2_statistic:.2f}')

# Label axes and add legend
plt.xlabel('Chi-square Value')
plt.ylabel('Probability Density')
plt.title('Chi-square Distribution')
plt.legend()

# Show the plot
plt.grid()
plt.show()

