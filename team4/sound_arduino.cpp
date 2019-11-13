long item;



void setup()

{

  item = 0;

  Serial.begin(9600);

  pinMode(5, OUTPUT);

}



void loop()

{

  if (Serial.available() > 0) {

    item = String(Serial.readString()).toInt();

    switch (item) {

     case 1:

      tone(5,131);

      break;

     case 2:

      tone(5,131);

      break;

     case 3:

      tone(5,131);

      break;

    }



  }



}
