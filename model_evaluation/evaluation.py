import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("enriched_behavior_data.xlsx", sheet_name="Sheet1")

# Features and targets
features = ['age_group', 'tech_savviness', 'interests', 'device', 'action', 'items_added_to_cart', 'affluence_score']
targets = ['affluence_level', 'consumer_trait']
X = df[features]
y = df[targets]

# Train/test split (same as before)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load trained model
pipeline = joblib.load("models/inference_pipeline.pkl")

# Make predictions
y_pred = pipeline.predict(X_test)

# Convert predictions to DataFrame for clarity
y_pred_df = pd.DataFrame(y_pred, columns=targets)

# Evaluation for each target
for target in targets:
    print(f"\n🎯 Evaluation for: {target}")
    print("Accuracy:", accuracy_score(y_test[target], y_pred_df[target]))
    print("Classification Report:\n", classification_report(y_test[target], y_pred_df[target]))

    # Confusion matrix
    cm = confusion_matrix(y_test[target], y_pred_df[target])
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"Confusion Matrix: {target}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
