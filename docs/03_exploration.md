
---

## 📝 File: `docs/03_exploration.md`

```markdown
# Data Exploration

```python
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), cmap="coolwarm", annot=True)
plt.title("Feature Correlation")

df.hist(figsize=(15, 10))
plt.tight_layout()
plt.show()
