import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data (normal distribution)
np.random.seed(0)
data = np.random.normal(loc=0, scale=1, size=1000)

# Plot histogram with kernel density estimate
plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True, color='blue', bins=30)
plt.title('Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('data_distribution.png')