import subprocess
import re

class TempGetter:
    def get_current_temp()->float:
        raw_output = subprocess.check_output(['vcgencmd', 'measure_temp'])
        searched_exp = re.search('[0-9]+.[0-9]', raw_output.decode("utf-8"))
        
        if searched_exp:
            raw_temp = searched_exp.group(0)
            
            return float(raw_temp)
        
        return 0.0