void setup() {
  // Start the serial communication
  Serial.begin(400000);
}

void loop() {
  // Send a message over the serial port
  Serial.println("13052023102830,5.12,1478,123,4567,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1");
  //Serial.println("1352023102830,5.12,1478,123,456/Users/omarabdelghany/Downloads/pythonVscode/send/send.ino7,1,1,1,1,1,1,1,1,1,1,25.31,102,102,10.11,11.34,13.41,-0.92,21.12,-1.45,-8.36,-6.12,10.32,30.-4.13,-6.34,11.25,1,8,31.120413,29.034037,123456,1,1,1");

  delay(1000);
}