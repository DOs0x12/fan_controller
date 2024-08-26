import RPi.GPIO as GPIO

class Controller:
    def __init__(self):
        global fan_pin;
        fan_pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(fan_pin, GPIO.OUT)

    def switch_fan(self, current_state: bool)->bool:
        state = not current_state
        GPIO.output(fan_pin, state)
        print('info: the fan is switched to ', end='')
        print(state)
        
        return state
    
    def clean_up_pins(self):
        GPIO.cleanup()