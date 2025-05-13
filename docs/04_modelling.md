
---

## 📝 File: `docs/04_modelling.md`

```markdown
# Anomaly Detection Modeling

## Isolation Forest

```python
iso_forest = IsolationForest(contamination=0.05, random_state=42)
df['anomaly_iforest'] = iso_forest.fit_predict(df)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop(columns=['anomaly_iforest']))
oc_svm = OneClassSVM(nu=0.05, kernel='rbf', gamma=0.1)
df['anomaly_ocsvm'] = oc_svm.fit_predict(X_scaled)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)
df['pca1'], df['pca2'] = pca_data[:, 0], pca_data[:, 1]
