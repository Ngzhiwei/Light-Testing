#include <LM35.h>
String tiempo;
int x=0,y=0;
float temperatura;
LM35 temp(A0);

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);
  pinMode(A0, INPUT);
}

void loop() {
  if(Serial.available()){
    tiempo = Serial.readString();
    y = tiempo.toInt();
    Serial.flush();
  }
  while(x < y)
  {
      temperatura = temp.cel();
      Serial.println(temperatura);
      x = x + 1;
      delay(1000);
  }
  if(x == y)
  {
    x=0;
    y=0;
  }
}
