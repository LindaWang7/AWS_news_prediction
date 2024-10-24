import pandas as pd
import matplotlib.pyplot as plt

#load the CSV data
data = pd.read_csv('latency_results.csv')

#create a boxplot
plt.figure(figsize=(8, 6))
data.boxplot(column='response_time', by='test_case')
plt.title('AWS News Detection Latency Boxplot')
plt.xlabel('Test Cases')
plt.ylabel('Response Time (s)')
plt.suptitle('')
plt.tight_layout()

# Save the plot
plt.savefig('latency_boxplot.png')
plt.show()
plt.close()

# Calculate the average performance for each test case
avg_performance = data.groupby('test_case')['response_time'].mean()
print("Average Performance (in seconds):\n", avg_performance)
