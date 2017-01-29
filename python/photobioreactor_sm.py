from __future__ import print_function
from transitions import Machine
import RPi.GPIO as GPIO  

class LED(object): 
    def __init__(self, pin=11): 
        self.pin = pin
        self.init_board()

    def __enter(self, pin=11): 
        self.pin = pin
        self.init_board()
    
    def init_board(self): 
        # to use Raspberry Pi board pin numbers  
        GPIO.setmode(GPIO.BOARD)  
        # set up GPIO output channel  
        GPIO.setup(self.pin, GPIO.OUT)  

    def led_on(self): 
        print("Turning the GPIO pin to high") 
        GPIO.output(self.pin, GPIO.HIGH)

    def led_off(self): 
        print("Turning the GPIO pin to low") 
        GPIO.output(self.pin, GPIO.LOW)
    
    def get_state(self):
        GPIO.setup(self.pin, GPIO.IN)
        state = GPIO.input(self.pin)
        GPIO.setup(self.pin, GPIO.OUT)
        return state
        
    def __exit__(self, *a): 
        GPIO.cleanup()


class PhotobioreactorSM(object):
    states = ['on', 'off']
    def __init__(self, power_led): 
        self.power_led = power_led
        self.machine = Machine(model=self, states=PhotobioreactorSM.states, initial='off')
        self.machine.add_transition(trigger='turn_on', source='off', dest='on', before='power_on')
        self.machine.add_transition(trigger='turn_off', source='on', dest='off', before='power_off')

    def power_on(self): 
        print("Turning on the photobiorecator!") 
        self.power_led.led_on()

    def power_off(self): 
        print("Turning off the photobioreactor!")
        self.power_led.led_off()
