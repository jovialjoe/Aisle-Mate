
// Motor pins
const int leftMotorPin = 6;  // PWM pin for left motor
const int rightMotorPin = 5; // PWM pin for right motor
const int EAPin = 3;
const int EBPin = 4;
// Variables to store motor speeds
int leftMotorSpeed = 0;
int rightMotorSpeed = 0;

void setup() {
  pinMode(leftMotorPin, OUTPUT);
  pinMode(rightMotorPin, OUTPUT);
  pinMode(EAPin, OUTPUT);
  pinMode(EBPin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(EAPin,HIGH);
  digitalWrite(EBPin,LOW);

}

void loop() {
  // Check if data is available from the Raspberry Pi
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n'); // Read input as a string
    int lIndex = data.indexOf('L');            // Find 'L' for left motor
    int rIndex = data.indexOf('R');            // Find 'R' for right motor

    if (lIndex != -1 && rIndex != -1) {
      // Extract and parse motor speed values
      leftMotorSpeed = data.substring(lIndex + 1, rIndex).toInt();
      rightMotorSpeed = data.substring(rIndex + 1).toInt();

      // Set motor speeds
      analogWrite(leftMotorPin, leftMotorSpeed);
      analogWrite(rightMotorPin, rightMotorSpeed);
    }
  }
}
