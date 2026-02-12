import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

mlflow.start_run()

df = pd.read_csv("data/data.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = LogisticRegression()
model.fit(X, y)

preds = model.predict(X)
acc = accuracy_score(y, preds)

mlflow.log_metric("accuracy", acc)
mlflow.sklearn.log_model(model, "model")

mlflow.end_run()

print("Training complete")