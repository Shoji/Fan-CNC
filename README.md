# Fan-CNC
This is a program I created to allow me to turn a fan in my room on / off.

The reason this code is not turning a fan connected to the arduino is because I currently done have access to a fan that can connect to the arduino so I just made do with what I have. In the future I will be making it compatible with a fan. 

The first part to this is installing and editing what is needed. Currently on the .py program anyone who wants to change the port will need to identify it through the Arduino IDE. Edit line 5 with your port which is located here: https://prnt.sc/jqeows

You will need to set up a basic circuit where the led is being powered through Digital Pin 10.
https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Arduino-LED-Circuit.gif > The schematic used to correctly power the led.

After that you need to upload the sketch to the arduino, then open the python program through the command line and execute it.

