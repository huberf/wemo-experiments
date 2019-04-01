import subprocess
import pywemo
import time
import json

config = json.loads(open('config.json').read())


def battery_percent():
    # Only works on OS X
    info = str(subprocess.check_output(['pmset', '-g', 'batt']))
    info = info.split(')\\t')[1]
    info = info.split('%')[0]
    return int(info)

## PROVISION WEMO
ip = config['main']['ip']
port = pywemo.ouimeaux_device.probe_wemo(ip)
url = 'http://%s:%i/setup.xml' % (ip, port)
device = pywemo.discovery.device_from_description(url, None)

charging_ceil = 90
charging_floor = 50

state = None
# Set baseline
percent = battery_percent()
if percent < charging_ceil:
    state = True
    device.on()
else:
    state = False
    device.off()

print('Set up and running...')

while True:
    time.sleep(5) # Don't need to be super responsive
    percent = battery_percent()
    if percent >= charging_ceil and state == True:
        state = False
        print('Toggling off')
        device.off()
    if percent <= charging_floor and state == False:
        state = True
        print('Toggling on')
        device.on()
    activity_log.log('batteryPercent', percent, 'Mac battery percentage')

