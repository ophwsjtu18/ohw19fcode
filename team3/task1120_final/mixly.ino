#include <Servo.h>

Servo servo_2;
Servo servo_4;
Servo servo_7;
Servo servo_8;
volatile int item;
volatile int item2;

void setup(){
  item2 = 90;
  item = 3;
  Serial.begin(9600);
  Serial.begin(9600);
  servo_2.attach(2);
  servo_8.attach(8);
  servo_4.attach(4);
  servo_7.attach(7);
}

void loop(){
  if (Serial.available() > 0) {
    item = String(Serial.readString()).toInt();

  }
  if (item == 1) {
    Serial.print(item);
    item2 = item2 + 10;
    servo_2.write(item2);
    delay(1000);

  } else if (item == 2) {
    item2 = item2 - 10;
    Serial.print(item);
    servo_2.write(item2);
    delay(1000);
  } else if (item == 0) {
    servo_8.write(60);
    delay(1000);
    servo_8.write(90);
    delay(1000);
    servo_4.write(35);
    delay(2000);
    servo_7.write(0);
    delay(1000);
    servo_4.write(90);
    delay(2000);
    servo_7.write(90);
    delay(2000);
  }

}