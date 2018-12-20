int receivedNum;
int dataNum[4];
boolean newData = false;
int doneReading = 0;
int i = 0;

void setup() {
    Serial.begin(9600);
    Serial.println("<Arduino is ready>");
}

void loop() {
  if (Serial.available() > 0) {
    recvOneChar();
  }
  else{
    if (doneReading == 3500)
    {
      showNewData();
      doneReading = 0;
    }
    else
    {
      doneReading++;
    }
  }
}

void recvOneChar() {
    if (Serial.available() > 0) {
        receivedNum = Serial.read();
        if (receivedNum > 47 && receivedNum < 59)
        {
          // Inputting data to be send in big endian order
          dataNum[i] = int(receivedNum);
          if (i < 4)
            i++;
          else
            i = 0;
          newData = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
        Serial.print("Contents of Array: ");
        for(int i = 0; i < 4; i++)
        {
          Serial.print(dataNum[i]);
          Serial.print(" ");
          
        
     
        }
        Serial.print("\n");
        newData = false;
        
    }

    
}
