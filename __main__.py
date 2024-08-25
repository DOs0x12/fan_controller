import metrics
import temp
import watcher
import sys
import signal

def main():
    metricPort = 8081
    metric_service = metrics.Service(metricPort)
    print('info: the service of metrics is started')
    reg_interruption()
    watcher.watch_temp(metric_service, temp.TempGetter)

def signal_handler(sig, frame):
    print('\ninfo: the temperature watching is interrupted')
    sys.exit(0)

def reg_interruption():
    for sig in [signal.SIGINT, signal.SIGTERM]:
        signal.signal(sig, signal_handler)

if __name__ == '__main__':
    main()