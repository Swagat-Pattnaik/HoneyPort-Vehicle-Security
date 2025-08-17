from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

# Features: [RSSI, Pulse Length, Noise Level]
# 0 = Safe, 1 = Attack
X = [
    [-55, 150, 0.4], [-52, 160, 0.3], [-58, 140, 0.5], [-53, 155, 0.45],  # Safe
    [-25, 300, 1.8], [-30, 320, 1.7], [-20, 310, 2.0], [-28, 305, 1.6]   # Attack
]
y = [0, 0, 0, 0, 1, 1, 1, 1]

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Save model properly
with open("phantom_rf_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("✅ Model trained and saved as phantom_rf_model.pkl")
