import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
csv_file_path = 'C:\\Users\\nisch\\Desktop\\jupyter\\Data LIWC 01 02 23.csv'
social_media_data = pd.read_csv(csv_file_path)

# Define a function to plot the distribution of engagement metrics
def plot_engagement_distribution(data, columns, title):
    data[columns].plot(kind='hist', subplots=True, layout=(2, 2), bins=20, figsize=(12, 8), sharex=False)
    plt.suptitle(title)
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()

# List of engagement metric columns
engagement_columns = ['retweet_count', 'reply_count', 'like_count', 'quote_count']

# Plot the distribution of engagement metrics
plot_engagement_distribution(social_media_data, engagement_columns, 'Distribution of Engagement Metrics')

# Calculate the correlation matrix for the engagement metrics
correlation_matrix = social_media_data[engagement_columns].corr()

# Plot the correlation matrix
plt.figure(figsize=(8, 6))
plt.title('Correlation Matrix of Engagement Metrics')
corr_heatmap = plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none', aspect='auto')
plt.colorbar(corr_heatmap)
plt.xticks(range(len(engagement_columns)), engagement_columns, rotation=45)
plt.yticks(range(len(engagement_columns)), engagement_columns)
plt.show()

# Display the correlation matrix values
print(correlation_matrix)
