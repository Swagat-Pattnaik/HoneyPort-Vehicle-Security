import serial
import time

try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2)  # Wait for Arduino to initialize

    if arduino.is_open:
        print("✅ Arduino connected on COM4")
        arduino.write(b'TRAP_ON\n')
        print("🔴 Laser ON (TRAP_ON sent)")
        time.sleep(5)
        arduino.write(b'TRAP_OFF\n')
        print("🟢 Laser OFF (TRAP_OFF sent)")
        arduino.close()
    else:
        print("❌ Arduino port not open.")

except serial.SerialException as e:
    print("❌ Error connecting to Arduino:", e)
