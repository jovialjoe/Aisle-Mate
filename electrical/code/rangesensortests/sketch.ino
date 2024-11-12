const int trigPin = 9;
const int echoPin = 8;

const int redLEDPin = 3;
const int greenLEDPin = 4;

const int distanceThreshold = 100;

void setup() {
  Serial.begin(9600);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(redLEDPin, OUTPUT);
  pinMode(greenLEDPin, OUTPUT);
}

void loop() {
  int distance = getAverageDistance();

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance <= distanceThreshold) {
    digitalWrite(redLEDPin, HIGH);
    digitalWrite(greenLEDPin, LOW);
  } else {
    digitalWrite(redLEDPin, LOW);
    digitalWrite(greenLEDPin, HIGH);
  }

  delay(100);
}

int getAverageDistance() {
  long sum = 0;
  const int numReadings = 5; 

  for (int i = 0; i < numReadings; i++) {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
  
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
  
    long duration = pulseIn(echoPin, HIGH);
  
    int distance = duration * 0.034 / 2;
    sum += distance;

    delay(10);
  }

  return sum / numReadings;
}
