#include <Servo.h>

#define servo_5_pin 5;
#define servo_9_pin 9;
#define servo_7_pin 7;
const int servo_9_angle = 90;
const int servo_7_angle = 80;
int item;                     //用于判定是投石头还是转角度

Servo servo_9;
Servo servo_5;
Servo servo_7;
int angle_serial;

void setup()
{
  Serial.begin(9600);
  servo_9.attach(9);
  servo_5.attach(5);
  servo_7.attach(7);
  delay(500);             //500是让板子缓冲，然后执行动作
  servo_5.write(0);
  servo_9.write(130);
  servo_7.write(0);
}

void loop()
{
  servo_5_or_9_angle(servo_5,servo_9);
}

void servo_5_or_9_angle(Servo servo_5,Servo servo_9)
{   
    item = String(Serial.readString()).toInt();
    //判定是进行转角度还是发射弹丸
    if (item != 30)
    {                   //1
      servo_5.write(item);
    }                   //1
    
    if (item == 30)
    {       //2
      
       servo_9.write(90);
       delay(1000);
       servo_7.write(servo_7_angle);
       delay(1000);
      
       servo_9.write(130);
       delay(500);
       servo_7.write(0);
       
    }       //2
