import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(data, column, bins=10):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=bins, palette='Set2')  
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

def bargraphs (col, data):     
    plt.figure(figsize=(10, 6))
    sns.countplot(x=col, data=data, palette='Set2')
    plt.title(f'Distribution of {col}')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

def trends(row):
    plt.figure(figsize=(12, 6))
    row.dt.year.value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title(f'Distribution of {row.name}')
    plt.xlabel(f'{row.name}')
    plt.ylabel('Frequency')
    plt.show()

def boxplots (column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=column)
    plt.title(f'Distribution of {column.name}')
    plt.show()