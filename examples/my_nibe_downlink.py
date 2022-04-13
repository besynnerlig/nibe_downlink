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
  
