import pywemo
import time
import json
import sys

config = json.loads(open('config.json').read())
ip = config['main']['ip']

port = pywemo.ouimeaux_device.probe_wemo(ip)

if port == None:
    print('Couldn\'t connect. Forcing exit...')
    sys.exit()

url = 'http://%s:%i/setup.xml' % (ip, port)

device = pywemo.discovery.device_from_description(url, None)


# Control loop
print('Set up and running...')

while True:
    in_ = input('On? [y/n]')
    if in_[0] == 'y':
        device.on()
    else:
        device.off()
