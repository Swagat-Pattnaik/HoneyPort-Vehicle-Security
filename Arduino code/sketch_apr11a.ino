#define LASER_PIN 9
#define BUZZER_PIN 10
#define BUTTON_PIN 7

void setup() {
  Serial.begin(9600);
  pinMode(LASER_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);  // Using internal pull-up resistor

  digitalWrite(LASER_PIN, LOW);   // Laser off by default
  digitalWrite(BUZZER_PIN, LOW);  // Buzzer off by default
}

void loop() {
  // 1. Listen to Serial Commands from Python
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();  // Remove any whitespace/newlines

    if (command == "TRAP_ON") {
      digitalWrite(LASER_PIN, HIGH);
      digitalWrite(BUZZER_PIN, HIGH);
      Serial.println("⚠️ TRAP ACTIVATED: Laser + Buzzer ON");
    } 
    else if (command == "TRAP_OFF") {
      digitalWrite(LASER_PIN, LOW);
      digitalWrite(BUZZER_PIN, LOW);
      Serial.println("✅ TRAP DEACTIVATED: Laser + Buzzer OFF");
    }
  }

  // 2. Monitor Button Press (Fake OBD port trigger)
  if (digitalRead(BUTTON_PIN) == LOW) {
    delay(200);  // Simple debounce
    Serial.println("OBD_HACK_ATTEMPT");  // Send to Python
    delay(1000);  // Wait a bit before next trigger
  }
}
