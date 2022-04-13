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

Create a configuration file, ~/nibe_downlink/config.py and add code from the [example config file](https://raw.githubusercontent.com/besynnerlig/nibe_downlink/master/examples/config.py).

Modify the configuration file to suit your needs.

Create your main python file, ~/nibe_downlink/my_nibe_downlink.py and add code from the [example file](https://raw.githubusercontent.com/besynnerlig/nibe_downlink/master/examples/my_nibe_downlink.py).

Modify the main python file file to suit your needs. Normally you can use it as it is, there's nothing to change.

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


### Nibe Uplink -> MQTT bridge service (Original example by the original author)

See *examples/mqtt.py*
