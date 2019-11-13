long item;
#define BuzzerPin6 6
#define BuzzerPin8 8
#define sleep_time 500
void setup()
{
  item = 0;
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0) {
    item = String(Serial.readString()).toInt();
    switch (item) {
     case 1:
      tone(BuzzerPin6,523);
      delay(sleep_time);
      break;
     case 2:
      tone(BuzzerPin6,587);
      delay(sleep_time);
      break;
     case 3:
      tone(BuzzerPin6,659);
      delay(sleep_time);
      break;
     case 4:
      tone(BuzzerPin6,698);
      delay(sleep_time);
      break;
     case 5:
      tone(BuzzerPin6,784);
      delay(sleep_time);
      break;
     case 6:
      tone(BuzzerPin6,880);
      delay(sleep_time);
      break;
     case 7:
      tone(BuzzerPin6,988);
      delay(sleep_time);
      break;
     case 8:
      tone(BuzzerPin6,1046);
      delay(sleep_time);
      break;
    }
    noTone(BuzzerPin6);

  }

}
