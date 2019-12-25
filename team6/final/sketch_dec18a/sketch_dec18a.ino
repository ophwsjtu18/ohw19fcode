#include <Servo.h>

Servo lockServo ; 
Servo armServo ; 
Servo bulletServo ; 
Servo directionServo ; 

void turnTo ( Servo servo , int from , int to  ) {
  
  if (from < to) {
    for (int i = from; i <= to; i ++) { 
      servo.write(i) ; 
      delay(15) ;                                
    }  
  } 
  else {
    for (int i = from; i >= to; i --) { 
      servo.write(i) ;  
      delay(15) ;                                   
    } 
  }
}

void bulletRelease() {
  
    turnTo(lockServo,lockServo.read(),130) ; 
    turnTo(armServo,armServo.read(),120) ;
    bulletClose() ; 
    delay(7) ;
    bulletOpen() ;
    delay(7) ; 
    bulletClose() ; 
    delay(2000) ;

}

void prepareToShoot() {
  turnTo(lockServo,lockServo.read(),60) ; 
  turnTo(armServo,armServo.read(),45) ; 
}

void shoot() {
  turnTo(lockServo,lockServo.read(),130) ; 
}

void bulletClose(){
  turnTo(bulletServo,bulletServo.read(),145) ; 
}

void bulletOpen() {
  turnTo(bulletServo,bulletServo.read(),100) ; 
}

void setup() {

  lockServo.attach(3) ; 
  armServo.attach(5) ; 
  bulletServo.attach(6) ;
  directionServo.attach(9) ; 
  bulletClose();
  delay(2500); 
  Serial.begin(9600);   
  
}

void loop() {
  
   bulletRelease(); 
   prepareToShoot() ;
   while( true ){
     if (Serial.available() > 0) {
     int angle = 0;
     angle = String(Serial.readString()).toInt();
     if( angle == 10000 ) { 
       shoot();
       bulletRelease();
       break;
     }
     else{ 
       if ( angle < 0 ) { 
       directionServo.write(directionServo.read()+2);               
       }
       if ( angle > 0 ) { 
       directionServo.write(directionServo.read()-2); 
       }
     }
     }
    }
    Serial.println(armServo.read());
}
