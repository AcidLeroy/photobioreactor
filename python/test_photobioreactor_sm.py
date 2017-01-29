import photobioreactor_sm as pbr

class DummyLED(): 
    def __init__(self, **kwargs): 
        pass
    def led_on(self): 
        print("Turning LED on!")
    def led_off(self): 
        print("Turning LED off!")

def test_status_led(): 
    led = DummyLED()
    sm = pbr.PhotobioreactorSM(led)
    assert "off" == sm.state
    sm.turn_on()
    assert "on" == sm.state
    sm.turn_off()
    assert "off" == sm.state

