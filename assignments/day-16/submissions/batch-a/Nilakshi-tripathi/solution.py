import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# Dataset

customer_data = {
    "customer_id": list(range(1, 22)),
    "annual_income": [
        15, 18, 16, 22, 19, 14, 20,
        44, 48, 46, 52, 49, 45, 50,
        78, 82, 80, 88, 85, 76, 90,
    ],
    "spending_score": [
        20, 25, 18, 30, 22, 15, 28,
        48, 52, 50, 58, 55, 46, 53,
        82, 88, 78, 90, 85, 80, 92,
    ],
}

df = pd.DataFrame(customer_data)


# Q1: Inspect Data

print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())


# Q2: Features

X = df[["annual_income", "spending_score"]]
print(X.head())

# customer_id is only an identifier, not a behavioral feature


# Q3: Elbow Method

inertias = []

for k in range(1, 8):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertia = model.inertia_
    inertias.append(inertia)
    print(f"k={k}, inertia={round(inertia, 2)}")

plt.plot(range(1, 8), inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_curve.png")
plt.close()


# Q4: Final KMeans Model

model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(X)

print(df)
print(df["cluster"].value_counts())

# clusters are labels, not ranks


# Q5: Centroids

centroids = model.cluster_centers_
print("Centroids (Income, Spending):")
print(np.round(centroids, 2))


# Q6: Visualization

plt.scatter(df["annual_income"], df["spending_score"], c=df["cluster"])
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    s=200,
    c="red",
    marker="X",
    label="Centroids"
)

plt.title("Customer Clusters")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.colorbar()
plt.tight_layout()
plt.savefig("customer_clusters.png")
plt.close()


# Q7: Silhouette Score

score = silhouette_score(X, df["cluster"])
print(round(score, 3))


# Q8: Business Insights

summary = df.groupby("cluster")[["annual_income", "spending_score"]].mean()
print(summary)

high_spend = summary["spending_score"].idxmax()
high_income = summary["annual_income"].idxmax()

print("Highest spending cluster:", high_spend)
print("Highest income cluster:", high_income)
print("Discount cluster:", summary["spending_score"].idxmin())
print("Premium cluster:", summary["annual_income"].idxmax())


# Q9: Save Model

joblib.dump(model, "kmeans_model.pkl")
print("Model saved as kmeans_model.pkl")