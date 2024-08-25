import metrics
import temp
import time
import fan

def watch_temp(metric_service: metrics.Service,
               temp_getter: temp.TempGetter,
               controller: fan.Controller):
    does_fan_work = False

    while True:
        temp = temp_getter.get_current_temp()
        metric_service.write_temp_metric(temp)

        if need_to_switch_fan(temp, does_fan_work):
            does_fan_work = controller.switch_fan(does_fan_work)

        time.sleep(60)

def need_to_switch_fan(temp: float, does_fan_work: bool)->bool:
    temp_upper_threshold = 75.0
    temp_lower_threshold = 55.0
    
    if temp >= temp_upper_threshold and  not does_fan_work:
        return True
    
    if temp < temp_lower_threshold and does_fan_work:
        return True
    
    return False
