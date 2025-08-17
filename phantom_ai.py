import serial
import threading
import time
import pickle
import os

# Load the trained AI model
try:
    with open("phantom_rf_model.pkl", "rb") as f:
        model = pickle.load(f)
    print("✅ AI model loaded.")
except Exception as e:
    print("❌ Failed to load AI model:", e)
    exit()

# Connect to Arduino
try:
    arduino = serial.Serial('COM4', 9600, timeout=1)  # Change COM3 to your port if needed
    print("✅ Arduino connected.")
except:
    arduino = None
    print("❌ Arduino not connected.")

# Trigger HoneyTrap
def trigger_honeytrap():
    print("\n🚨 AI: Relay Attack Detected!")
    print("🔒 HoneyTrap activated (LED + Buzzer)")
    if arduino:
        arduino.write(b'TRAP_ON\n')
    print("📍 Location: https://maps.google.com/?q=12.9716,77.5946")
    print("📩 Owner alerted!")

# Turn off trap (optional)
def turn_off_trap():
    if arduino:
        arduino.write(b'TRAP_OFF\n')
        print("🟢 HoneyTrap deactivated.")

# Classify signal with AI
def classify_signal(rssi, pulse_length, noise_level):
    features = [[rssi, pulse_length, noise_level]]
    prediction = model.predict(features)[0]
    return prediction  # 1 = attack, 0 = safe

# Listen to Arduino OBD trap
def listen_to_arduino():
    while True:
        if arduino and arduino.in_waiting:
            line = arduino.readline().decode().strip()
            if line == "OBD_HACK_ATTEMPT":
                print("\n💀 THIEF plugged into fake OBD port!")
                # Simulated attacker signal values
                prediction = classify_signal(-25, 300, 1.8)
                if prediction == 1:
                    trigger_honeytrap()
                else:
                    print("🟢 AI: Signal is safe. No action taken.")

# Manual test mode
def test_manual_case():
    print("\n🧪 TEST MODE:")
    print("1. Simulate Safe Signal")
    print("2. Simulate Attack Signal")
    choice = input("Select option (1 or 2): ")

    if choice == "1":
        features = [-55, 150, 0.4]  # Safe signal
        print("\n✅ Sending SAFE signal...")
    elif choice == "2":
        features = [-25, 300, 1.8]  # Attack signal
        print("\n🚨 Sending ATTACK signal...")
    else:
        print("❌ Invalid choice.")
        return

    prediction = classify_signal(*features)
    if prediction == 1:
        trigger_honeytrap()
    else:
        print("🟢 AI: Signal is safe. No action taken.")

# Start listening in background
if arduino:
    threading.Thread(target=listen_to_arduino, daemon=True).start()

# Main loop
print("\n🧠 PhantomKey AI Anti-Theft System Armed")

while True:
    print("\n===============================")
    print("1. Wait for OBD Trap (Press the Button)")
    print("2. Test with Manual Signal (Safe/Attack)")
    print("3. Turn Off HoneyTrap")
    print("4. Exit")
    option = input("Choose (1/2/3/4): ")

    if option == "1":
        print("📡 Listening for OBD attack...")
        while True:
            time.sleep(1)
    elif option == "2":
        test_manual_case()
    elif option == "3":
        turn_off_trap()
    elif option == "4":
        print("👋 Exiting...")
        turn_off_trap()
        break
    else:
        print("❌ Invalid option.")
