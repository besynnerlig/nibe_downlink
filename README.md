# Nibe Downlink to MQTT
Get variables from Nibe Uplink and publish on MQTT. Modified to work with python3.

# Requirements
Your heatpump should be registered in Nibe Uplink. This module fetches data from Nibe Uplink

# Installation

    mkdir ~/nibe_downlink&&cd ~/nibe_downlink
    python3 -m venv env
    source env/bin/activate 
    pip install git+https://github.com/besynnerlig/nibe_downlink.git
    pip install requests
    pip install paho-mqtt

Create ~/nibe_downlink/config.py and add the following code. Modify to suit your needs.

``` python
import logging

rootLogger = logging.getLogger()
rootLogger.addHandler(logging.StreamHandler())
rootLogger.setLevel(logging.DEBUG)

MQTT_CONF = {
  #'auth': { # This block can be skipped if you do not have auth on your mqtt
  #  "username": "",
  #  "password": ""
  #},
  'hostname': "XXXXXX", # MQTT IP address or hostname
  'prefix': 'nibeuplink/YOURHEATPUMPMODELL'
}

NIBE_UPLINK_CONF = {
  'username': "YOUR-EMAIL",
  'password': "YOUR-PASSWORD",
  "hpid": "HEAT-PUMP-ID", # heat pump id
  'variables': [40004, 40013, 40014, 40033, 40047, 40048, 43005, 43009, 43084, 43427] # variables you want to fetch
}    
```

Create ~/nibe_downlink/my_nibe_downlink.py and add the following code. Modify to suit your needs.

``` python
#!/home/YOURUSERNAME/nibe_downlink/env/bin/python
import sys

import logging
import time
from nibe_downlink import NibeDownlink

from paho.mqtt.client import Client as MQTTClient
from config import NIBE_UPLINK_CONF, MQTT_CONF

last_values = {}
for v in NIBE_UPLINK_CONF['variables']:
  last_values[str(v)] = ''

last_values['online'] = ''
logger = logging.getLogger()

nd = NibeDownlink(**NIBE_UPLINK_CONF)
mqtt_client = MQTTClient()
if 'auth' in MQTT_CONF:
  mqtt_client.username_pw_set(**MQTT_CONF['auth'])
mqtt_client.connect(MQTT_CONF['hostname'])
mqtt_client.loop_start()

while True:
  try:
    online, values = nd.getValues()
    # print values
    if online != last_values['online']:
      mqtt_client.publish(MQTT_CONF['prefix'] + '/online', 1 if online else 0, retain=True)
      last_values['online'] = online

    if values:
      for key, value in values.items():
        if value != last_values[str(key)]:
          mqtt_client.publish(MQTT_CONF['prefix'] + '/variables/' + str(key), value, retain=True)
          last_values[str(key)] = value
    else:
      logger.exception("Failed to get Nibe uplink values")
      break

  except Exception as e:
    logger.exception("Exception while fetching Nibe uplink values")
  time.sleep(60)
```

Set permissions
```
sudo chmod 755 /home/YOURUSERNAME/nibe_downlink/my_nibe_downlink.py
```

# Optional installation
    sudo npm install pm2@latest -g
    Set up pm2 to watch that yor script never dies (Not covered here). However this is the command line I used to add the script to pm2:
    ```pm2 start /home/YOURUSERNAME/nibe_downlink/my_nibe_downlink.py --name nibe-downlink --interpreter /home/YOURUSERNAME/nibe_downlink/env/bin/python --restart-delay=60000```

# Usage

Test run the code

```
/home/YOURUSERNAME/nibe_downlink/my_nibe_downlink.py
```

If it works you'd like to set it up so that it runs in the background and starts automatically when the server boots. There's several ways to achieve that. Using pm2 works well for me. 

### Heat Pump ID: hpid
Get your **hpid** from Nibe Uplink web site. Open a heatpump and it's id will be in your address bar:
https://www.nibeuplink.com/System/**99999**/Status/Overview

### Variable IDs
See https://github.com/openhab/openhab1-addons/wiki/Nibe-Heat-Pump-Binding

# Examples

Copy *examples/config.py.dist* to *examples/config.py* and change settings inside the file

### Nibe Uplink -> MQTT bridge service

See *examples/mqtt.py*
