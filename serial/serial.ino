#include <Servo.h>
Servo myservo;
const int trigPin = 6;
const int echoPin = 5;
float Distance() {
   
  pinMode(trigPin, OUTPUT);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
   
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
   
  pinMode(trigPin, INPUT);
  
   
  float duration = pulseIn(echoPin, HIGH);
  
 
  float distance = duration * 0.034 / 2;
  return distance;
}

void setup() {
  myservo.attach(9);
  pinMode(5,INPUT);
  pinMode(6,OUTPUT);
  Serial.begin(9600);

  // put your setup code here, to run once:

}

void loop() {
  if(Serial.available()){
    char t = Serial.read();
    if(t=='l'){
      myservo.write(0);
    }
    else if(t=='r'){
      myservo.write(180);
    }
    else{
      myservo.write(90);
    }
  }

}
