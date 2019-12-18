#include <IRremote.h>

#include <Servo.h>

IRrecv irrecv_10(10);
decode_results results_10;

Servo servo_2;
Servo servo_4;
Servo servo_7;
Servo servo_8;
long ir_item;
volatile int item;
volatile int item2;
volatile int mode;
volatile int temp;

void setup(){
  item2 = 90;
  item = 3;
  temp = 3;
  mode = 3;
  Serial.begin(9600);
  Serial.begin(9600);
  servo_2.attach(2);
  servo_8.attach(8);
  servo_4.attach(4);
  servo_7.attach(7);
  irrecv_10.enableIRIn();
}

void loop(){
  if (Serial.available() > 0) {
    temp = String(Serial.readString()).toInt();
    if (temp > 4 && temp < 8) {
      mode = temp;

    } else {
      if (temp >= 0 && temp <= 3) {
        item = temp;

      }

    }

  }
  if (mode == 5) {
    if (item == 1) {
      Serial.print(item);
      item2 = item2 + 10;
      servo_2.write(item2);
      delay(500);

    } else if (item == 2) {
      item2 = item2 - 10;
      Serial.print(item);
      servo_2.write(item2);
      delay(500);
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
      item = 3;
    }

  }
  if (mode == 6) {
    if (irrecv_10.decode(&results_10)) {
      ir_item=results_10.value;
      String type="UNKNOWN";
      String typelist[14]={"UNKNOWN", "NEC", "SONY", "RC5", "RC6", "DISH", "SHARP", "PANASONIC", "JVC", "SANYO", "MITSUBISHI", "SAMSUNG", "LG", "WHYNTER"};
      if(results_10.decode_type>=1&&results_10.decode_type<=13){
        type=typelist[results_10.decode_type];
      }
      Serial.print("IR TYPE:"+type+"  ");
      Serial.println(ir_item);
      switch (ir_item) {
       case 16716015:
        item2 = item2 - 20;
        servo_2.write(item2);
        delay(100);
        break;
       case 16734885:
        item2 = item2 + 20;
        servo_2.write(item2);
        delay(100);
        break;
       case 16726215:
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
        break;
      }
      irrecv_10.resume();
    } else {
    }

  }

}