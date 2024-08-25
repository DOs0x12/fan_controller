import prometheus_client

class Service:
    def __init__(self, port: int):
        prometheus_client.start_http_server(port)
        global __metric_gauge
        __metric_gauge = prometheus_client.Gauge('cpu_temperature_celcius', 'The current CPU temperature')

    def write_temp_metric(self, temp: float):
        __metric_gauge.set(temp)