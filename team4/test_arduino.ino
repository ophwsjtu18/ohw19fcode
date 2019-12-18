#include <Servo.h>


#define servo_9_pin 9;
#define servo_5_pin 5;
int servo_9_angle = 90;
int item;
Servo servo_9;
Servo servo_5;
void setup() {
  Serial.begin(9600);
  servo_9.attach(9);
  servo_5.attach(5);
  delay(500);             //500是让板子缓冲，然后执行动作


}

void loop() {
  if ((item = String(Serial.readString()).toInt()) == 1)
  {
  servo_9.write(180);
  delay(1000);
  servo_9.write(0);
  delay(1000);
}
    
    
    
  

  if ((item = String(Serial.readString()).toInt()) != 1){
    servo_5.write(item);
    
  }
  delay(500);

}
