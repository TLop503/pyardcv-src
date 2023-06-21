// L298N Motor Driver Pin Configuration
const int motorEN = 9;     // Enable pin (ENA) for PWM speed control
const int motorIN1 = 8;    // Input 1 (IN1) pin
const int motorIN2 = 7;    // Input 2 (IN2) pin

void setup() {
  pinMode(motorEN, OUTPUT);
  pinMode(motorIN1, OUTPUT);
  pinMode(motorIN2, OUTPUT);
  Serial.begin(9600);  // Set the baud rate to match the serial configuration
  while (!Serial) {
    ;  // Wait for the serial port to connect
  }
}

String data;

void loop() {
   if (Serial.available()) {
    data = Serial.readStringUntil('\n');
    data.trim();  // Remove leading and trailing whitespace
  }

  if (data == "left"){
    setMotorSpeed(50);  
    setMotorDirection(true);
  }
  else if (data == "right"){
    setMotorSpeed(50);  
    setMotorDirection(false);
  }
  else {
    setMotorSpeed(0);
  }
}

// Function to set the motor direction
void setMotorDirection(bool forward) {
  digitalWrite(motorIN1, forward);
  digitalWrite(motorIN2, !forward);
}

// Function to set the motor speed (PWM)
void setMotorSpeed(int speed) {
  analogWrite(motorEN, speed);
}
