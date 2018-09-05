#include <SPI.h> // Used for communication with the Sparkfun CAN-bus Shield
#include "mcp_can.h" // Used to interperet the can-bus messages

/* OBDII Connector

 \  1  2  3  4  5  6  7  8  /
  \ 9 10 11 12 13 14 15 16 /

*/

//#define CAN_SPEED CAN_33KBPS
//Low Speed CAN 33.3kbps
//LSCAN-H - 1
//LSCAN-L - GND - 5

#define CAN_SPEED CAN_95KBPS // Used by my car's steering wheel
//Medium Speed CAN 95kbps
//MSCAN-H - 3
//MSCAN-L - 11

//#define CAN_SPEED CAN_500KBPS
//High Speed CAN 500kbps
//HSCAN-H - 6
//HSCAN-L - 14

MCP_CAN CAN(10); // The SPI chip select pin. D10 in case of the Sparkfun CAN-bus Shield. I know some other shields use D9. 

INT32U canId = 0x000;
unsigned char len = 0;
unsigned char buf[8];

// For memory
//unsigned char STEERING_WHEEL_NEXT[3] = {0x1, 0x91, 0x0};
//unsigned char STEERING_WHEEL_PREVIOUS[3] = {0x1, 0x92, 0x0};
//unsigned char STEERING_WHEEL_RELEASE[3] = {0x1, 0x0, 0x0};

void setup() {

  // Open the serial port for communication
  Serial.begin(115200);

  // Try to connect to the Sparkfun CAN-bus shield
  START_INIT:
  if (CAN_OK == CAN.begin(CAN_SPEED)) {
    Serial.println("CAN BUS Shield init ok!");
  } else {
    delay(500);
    Serial.println("CAN BUS Not Connected");
    goto START_INIT;
  }

}

void loop() {

  // Check CAN BUS
  if (CAN_MSGAVAIL == CAN.checkReceive()) { // Check if data is comming on the can-bus (in MCP2515 cache)
    CAN.readMsgBuf( & len, buf); // Read a frame
    canId = CAN.getCanId(); // Get the sender id from the frame

    // Filter out all frames from the steering wheel
    if (canId == 0x206) { // == steering wheel module

      if (buf[0] == 0x1 && buf[1] == 0x91 && buf[2] == 0x0) { // Media NEXT Button
        Serial.println("MEDIA-NEXT");
      } else if (buf[0] == 0x1 && buf[1] == 0x92 && buf[2] == 0x0) { // Media PREVIOUS Button
        Serial.println("MEDIA-PREVIOUS");
      } else if (buf[0] == 0x1 && buf[1] == 0x0 && buf[2] == 0x0) { // RELEASE of a Button
        Serial.println("MEDIA-RELEASE");
      } else {
        Serial.println("OTHER-BUTTON");
      }

      // === Print all steering wheel data for debugging ===
      //Serial.print(canId, HEX);
      //Serial.print(" ");
      //for(int i = 0; i<len; i++){Serial.print(buf[i]);Serial.print(" ");}
      //Serial.println();

    }

    // === Print all raw data for debugging ===
    //Serial.print("ID: ");
    //Serial.print(canId, HEX);
    //Serial.print(", ");
    //Serial.print("Data: ");
    //for(int i = 0; i<len; i++){Serial.print(buf[i]);Serial.print("\t");}
    //Serial.println();
    
  }
 
}
