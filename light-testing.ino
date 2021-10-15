#include <LM35.h>
String tiempo;
int x=0,y=0;
float temperaturac, temperaturaf, temperaturak;
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
      temperaturac = temp.cel();
      temperaturaf = temp.fah();
      temperaturak = temp.kel();
      Serial.print(temperaturac);
      Serial.print(',');
      Serial.print(temperaturaf);
      Serial.print(',');
      Serial.println(temperaturak);
      x = x + 1;
      delay(1000);
  }
  if(x == y)
  {
    x=0;
    y=0;
  }
}
