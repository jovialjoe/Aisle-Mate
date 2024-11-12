// Pin definitions
const int encoderPinA = 12;  // Quadrature Encoder A signal
const int encoderPinB = 11;  // Quadrature Encoder B signal

// Variables to store the encoder count and direction
long encoderCount = 0;
int lastEncoderAState = LOW;

void setup() {
  // Set up encoder pins as inputs
  pinMode(encoderPinA, INPUT);
  pinMode(encoderPinB, INPUT);

  // Start serial communication for monitoring
  Serial.begin(9600);
}

void loop() {
  // Read the current state of encoder A
  int encoderAState = digitalRead(encoderPinA);
  int encoderBState = digitalRead(encoderPinB);

  // If encoder A's state has changed, it means a pulse has occurred
  if (encoderAState != lastEncoderAState) {
    // Determine the direction based on the state of encoder B
    if (encoderAState == HIGH) {
      if (encoderBState == HIGH) {
        encoderCount++;
      } else {
        encoderCount--;
      }
    } else {
      if (encoderBState == HIGH) {
        encoderCount--;
      } else {
        encoderCount++;
      }
    }
    
    // Print the encoder count
    Serial.print("Encoder Count: ");
    Serial.println(encoderCount);
  }

  // Update the last state of encoder A
  lastEncoderAState = encoderAState;

  // Optional delay to stabilize readings
}
