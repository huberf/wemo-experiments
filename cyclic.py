import pywemo
import time
import json
import sys
import time

config = json.loads(open('config.json').read())
ip = config['main']['ip']

port = pywemo.ouimeaux_device.probe_wemo(ip)

if port == None:
    print('Couldn\'t connect. Forcing exit...')
    sys.exit()

url = 'http://%s:%i/setup.xml' % (ip, port)

device = pywemo.discovery.device_from_description(url, None)

print('Set up and running...')

tick = 1
INTERVAL = 120

while True:
    if tick:
        device.on()
    else:
        device.off()
    time.sleep(INTERVAL)
    tick = (not tick)
