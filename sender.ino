#include  <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); //CNS, CE

const byte rxAddr[6] = "00001";
const int c = 261;
const int C = 277;
const int d = 294;
const int D = 311;
const int e = 330;
const int f = 349;
const int F = 370;
const int g = 392;
const int G = 415;
const int a = 440;
const int n = 100;

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.setRetries(15, 15);
  radio.openWritingPipe(rxAddr);
  radio.stopListening();
}

void loop() {
 char inByte = ' ';
 if (Serial.available()){
  char inByte = Serial.read();
  switch (inByte){
    case 'c':{
      radio.write(&c,sizeof(c));
      break;
    }
    case 'C':{
      radio.write(&C,sizeof(C));
      break;
    }
    case 'd':{
      radio.write(&d,sizeof(d));
      break;
    }
    case 'D':{
      radio.write(&D,sizeof(D));
      break;
    }
    case 'e':{
      radio.write(&e,sizeof(e));
      break;
    }
    case 'f':{
      radio.write(&f,sizeof(f));
      break;
    }
    case 'F':{
      radio.write(&F,sizeof(F));
      break;
    }
    case 'g':{
      radio.write(&g,sizeof(g));
      break;
    }
    case 'G':{
      radio.write(&G,sizeof(G));
      break;
    }
    case 'a':{
      radio.write(&a,sizeof(a));
      break;
    }
    case 'n':{
      radio.write(&n,sizeof(n));
      //Serial.println("received n");
      break;
    }
  }
}
}