# Python source code

For now, we can organize the code into two categories: 

1) Any code that directly communicates to the board e.g. GPIO, SPI, I2C. 
2) Any code that we use to communicate back to the AWS cloud

## Description of source code

- `led_blink.py` - This is the hello world application for turning LEDs on and off. 
- `photobioreactor_sm.py` - This code represents the state machine of the photobioreactor and all the state transitions. 
- `publish_status.py` - This is a sample program for publishing the curren state of the "power" to the LED and also
receive commands from the AWS IoT platform. This code **will not** work out of the box. You must point the path to the 
certificates that you have downloaded from amazon for this to work. You are welcome to change the publishing topics as 
well. 
