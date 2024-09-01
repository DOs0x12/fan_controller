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

        if controller.need_to_switch_fan(temp, does_fan_work):
            does_fan_work = controller.switch_fan(does_fan_work)

        time.sleep(60)
