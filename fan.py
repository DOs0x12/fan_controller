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
    
    def need_to_switch_fan(self, temp: float, does_fan_work: bool)->bool:
        temp_upper_threshold = 60.0
        temp_lower_threshold = 40.0
        
        if temp >= temp_upper_threshold and  not does_fan_work:
            return True
        
        if temp < temp_lower_threshold and does_fan_work:
            return True
        
        return False

    def clean_up_pins(self):
        GPIO.cleanup()