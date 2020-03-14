const byte stepPin = 7;
const byte directionPin = 8;
const byte enablePin = 11;
int data;   
int delayTime = 100;
int hours;


void setup() {
  Serial.begin(9600);
  pinMode(stepPin, OUTPUT);
  pinMode(directionPin, OUTPUT);
  pinMode(enablePin, OUTPUT);
}
void loop() {
    while (Serial.available())
    { 
        data = Serial.read();
        if (data == '1')
        {
          digitalWrite(enablePin, HIGH);
          digitalWrite(directionPin, HIGH);
          for (int i = 0; i < 1000; ++i) {
            // Делаем шаг
            digitalWrite(stepPin, HIGH);
            delay(delayTime);
            digitalWrite(stepPin, LOW);
            delay(delayTime);
            data = Serial.read();
            if (data == '3')
            {
               digitalWrite(enablePin, LOW);;
            }
            if (data == '0')
            {
              delayTime = delayTime - 10;
              digitalWrite(enablePin, HIGH);
          digitalWrite(directionPin, HIGH);
          for (int i = 0; i < 1000; ++i) {
            // Делаем шаг
            digitalWrite(stepPin, HIGH);
            delay(delayTime);
            digitalWrite(stepPin, LOW);
            delay(delayTime);
            data = Serial.read();
            }
            }
          }
        }
 
        }
    }
