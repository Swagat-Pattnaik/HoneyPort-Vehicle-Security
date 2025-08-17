# HoneyPort Vehicle Security 🚗🔐

### Overview
HoneyPort Vehicle Security is an **IoT-powered theft detection and rescue alert system** inspired by the **honeyport cybersecurity concept**.  
It monitors unauthorized access attempts to a vehicle’s control unit and triggers **real-time alerts** using IoT communication. The system integrates **Machine Learning models** with **Arduino hardware** to detect intrusions, generate data-driven insights, and prevent theft.

---

### 🔧 Tech Stack
- **Languages:** Python, C++ (Arduino)
- **Libraries:** NumPy, Pandas, Matplotlib, Scikit-learn, PySerial
- **Hardware:** Arduino microcontroller + sensors
- **Concepts:** Honeyport Security, IoT, Real-time Monitoring, ML-based Detection

---

### ⚙️ Features
- Detects **unauthorized vehicle access attempts** using honeyport traps.  
- Sends **real-time alerts** to owner/authorities via IoT communication.  
- **Machine Learning-based detection** trained with generated datasets.  
- Arduino integration for **real-time system response**.  
- Data visualization for monitoring intrusion trends.  

---

### 📂 Project Structure
HoneyPort-Vehicle-Security/
│── phantom_ai.py # Core AI/ML intrusion detection
│── phantom_data_generator.py # Generates training/testing data
│── phantom_model_trainer.py # Trains ML models
│── phantom_rf_data.csv # Sample dataset
│── phantom_rf_model.pkl # Saved trained model
│── test.py # Test script for evaluation
│── Arduino code/
│ └── sketch_apr11a.ino # Arduino program for IoT alerts
│── requirements.txt # Dependencies
│── README.txt # Documentation


📊 Results
Successfully detected intrusion attempts with high accuracy using Random Forest.
Enabled real-time alerts with Arduino + IoT.
Provided intrusion trend visualization for analysis.

