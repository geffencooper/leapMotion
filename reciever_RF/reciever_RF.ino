#include <SPI.h>  
#include <nRF24L01.h>
#include "RF24.h"

RF24 radio (7, 8); 

const byte address[6] = "00001"; 

void setup() 
{
  Serial.begin(9600);
  radio.begin(); 
  radio.openReadingPipe(0, address); 
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
  pinMode(4, OUTPUT);
}


void loop()  
{
  if (radio.available()) 
  {
    long text;
    radio.read(&text, sizeof(text));
    Serial.println(text);
    if(text!= 100){
      tone(4, text);
      delay(10);
    }
    else{
      noTone(4);
    }
  }

}
