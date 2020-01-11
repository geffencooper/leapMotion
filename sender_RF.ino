
#include  <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); //CNS, CE

const byte rxAddr[6] = "00001";
const int C = 261;
const int Cs = 277;
const int D = 294;
const int Ds = 311;
const int E = 330;
const int F = 349;
const int Fs = 370;
const int G = 392;
const int Gs = 415;
const int A = 440;
const int As = 466;
const int B = 494;
void setup() {
  radio.begin();
  radio.setRetries(15, 15);
  radio.openWritingPipe(rxAddr);
  radio.stopListening();
}

void loop() {
  radio.write(&C, sizeof(C));
  delay(1000);
  radio.write(&Cs, sizeof(Cs));
  delay(1000);
  radio.write(&D, sizeof(D));
  delay(1000);
  radio.write(&Ds, sizeof(Ds));
  delay(1000);
  radio.write(&E, sizeof(E));
  delay(1000);
  radio.write(&F, sizeof(F));
  delay(1000);
  radio.write(&Fs, sizeof(Fs));
  delay(1000);
  radio.write(&G, sizeof(G));
  delay(1000);
  radio.write(&Gs, sizeof(Gs));
  delay(1000);
  radio.write(&A, sizeof(A));
  delay(1000);
  radio.write(&As, sizeof(As));
  delay(1000);
  radio.write(&B, sizeof(B));
  delay(1000);
}
