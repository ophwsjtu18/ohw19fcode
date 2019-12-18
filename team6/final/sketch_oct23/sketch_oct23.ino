#include <IRremote.h>

#include <Servo.h>

IRrecv irrecv_11(11);
decode_results results_11;

Servo servo_5;
long ir_item;

void setup(){
  servo_5.attach(5);
  pinMode(6, OUTPUT);
  servo_5.write(90);
  delay(0);
  digitalWrite(6,LOW);
  Serial.begin(9600);
  irrecv_11.enableIRIn();
}

void loop(){
  if (irrecv_11.decode(&results_11)) {
    ir_item=results_11.value;
    String type="UNKNOWN";
    String typelist[14]={"UNKNOWN", "NEC", "SONY", "RC5", "RC6", "DISH", "SHARP", "PANASONIC", "JVC", "SANYO", "MITSUBISHI", "SAMSUNG", "LG", "WHYNTER"};
    if(results_11.decode_type>=1&&results_11.decode_type<=13){
      type=typelist[results_11.decode_type];
    }
    Serial.print("IR TYPE:"+type+"  ");
    Serial.println(ir_item,HEX);
    irrecv_11.resume();
  } else {
  }
  if (ir_item == 0xFF18E7) {
    servo_5.write(90);
    delay(0);
    digitalWrite(6,HIGH);

  }
  if (ir_item == 0xFF38C7) {
    servo_5.write(90);
    delay(0);
    digitalWrite(6,LOW);

  }
  if (ir_item == 0xFF10EF) {
    servo_5.write(70);
    delay(0);
    digitalWrite(6,HIGH);

  }
  if (ir_item == 0xFF5AA5) {
    servo_5.write(110);
    delay(0);
    digitalWrite(6,HIGH);

  }

}
