
---

## 📝 File: `docs/05_results.md`

```markdown
# Results and Visualization

## Isolation Forest PCA Plot

```python
plt.figure(figsize=(10,6))
sns.scatterplot(x='pca1', y='pca2', hue='anomaly_iforest', data=df, palette='coolwarm')
plt.title("Isolation Forest - PCA View")

plt.figure(figsize=(10,6))
sns.scatterplot(x='pca1', y='pca2', hue='anomaly_ocsvm', data=df, palette='coolwarm')
plt.title("One-Class SVM - PCA View")

df['combined'] = df.apply(lambda x: 'Both' if x.anomaly_iforest == x.anomaly_ocsvm else 'Mismatch', axis=1)
df['combined'].value_counts()
