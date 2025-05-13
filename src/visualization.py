import matplotlib.pyplot as plt
import seaborn as sns

# Isolation Forest Plot
def plot_iforest(df):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='pca1', y='pca2', hue='anomaly_iforest', data=df, palette='coolwarm')
    plt.title("Isolation Forest - PCA")
    plt.show()

# One-Class SVM Plot
def plot_ocsvm(df):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='pca1', y='pca2', hue='anomaly_ocsvm', data=df, palette='coolwarm')
    plt.title("One-Class SVM - PCA")
    plt.show()
