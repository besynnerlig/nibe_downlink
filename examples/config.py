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
