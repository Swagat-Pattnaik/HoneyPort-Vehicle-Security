import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Generate normal (safe) behavior
normal_signals = {
    "signal_strength": np.random.normal(loc=-50, scale=5, size=500),
    "pulse_width": np.random.normal(loc=150, scale=10, size=500),
    "frequency_noise": np.random.normal(loc=0.5, scale=0.1, size=500),
    "label": [0]*500  # 0 = normal
}

# Generate attack (relay spoofing) behavior
attack_signals = {
    "signal_strength": np.random.normal(loc=-30, scale=7, size=500),
    "pulse_width": np.random.normal(loc=300, scale=30, size=500),
    "frequency_noise": np.random.normal(loc=1.5, scale=0.3, size=500),
    "label": [1]*500  # 1 = attack
}

# Combine into a DataFrame
df = pd.DataFrame({key: np.concatenate([normal_signals[key], attack_signals[key]])
                   for key in normal_signals})

# Save as CSV for training
df.to_csv("phantom_rf_data.csv", index=False)
print("✅ Dataset created: phantom_rf_data.csv")

# Optional: Visualize
plt.figure(figsize=(8,6))
plt.scatter(df[df.label == 0]["signal_strength"], df[df.label == 0]["pulse_width"], alpha=0.6, label="Normal")
plt.scatter(df[df.label == 1]["signal_strength"], df[df.label == 1]["pulse_width"], alpha=0.6, label="Relay Attack")
plt.xlabel("Signal Strength (dBm)")
plt.ylabel("Pulse Width (ms)")
plt.title("Simulated Signal Data")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
