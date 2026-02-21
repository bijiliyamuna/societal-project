import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample dataset
data = {
    "plastic_type": [0,1,2,0,1,2],
    "quantity": [5,10,3,8,6,2],
    "recyclable": [1,1,0,1,1,0]
}

df = pd.DataFrame(data)

X = df[["plastic_type", "quantity"]]
y = df["recyclable"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "waste_model.pkl")

print("Model Created Successfully!")