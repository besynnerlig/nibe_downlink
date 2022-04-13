# Nibe Downlink to MQTT
Get variables from Nibe Uplink and publish on MQTT. Modified to work with python3.

# Requirements
Your heatpump should be registered in Nibe Uplink. This module fetches data from Nibe Uplink
Get your **hpid** from Nibe Uplink web site. Open a heatpump and it's id will be in your address bar:
https://www.nibeuplink.com/System/**99999**/Status/Overview

# Installation example (The following tested on Ubuntu 21.10)

    sudo apt-get update
    sudo apt-get install python3.9-venv git -y
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
You can alter what variable id:s you'd like it to fetch. See https://github.com/openhab/openhab1-addons/wiki/Nibe-Heat-Pump-Binding

Set permissions
```
sudo chmod 755 /home/YOURUSERNAME/nibe_downlink/my_nibe_downlink.py
```

Test run. It will run until you exit the script. Enter Ctrl-C when you have tested.
```
./my_nibe_downlink.py
```

Deactivate the python environment
```
deactivate
```

# Keep it running using PM2 (a daemon process manager)
This will help you manage and keep your application online 24/7

```
sudo apt-get install npm -y
sudo npm install pm2@latest -g
pm2 start /home/YOURUSERNAME/nibe_downlink/my_nibe_downlink.py --name nibe-downlink --interpreter /home/YOURUSERNAME/nibe_downlink/env/bin/python --restart-delay=60000
pm2 save
pm2 startup
```
Now, after the last command you shold have a command that you should copy and paste. Do that!

PM2 has an [excellent documentation](https://pm2.keymetrics.io/docs/usage/quick-start/). Read it if you encounter any issues.

# This is a forked project.
This project was forked from a work by Jevgeni Kiski, https://github.com/yozik04/nibe_downlink Thank you Jevgeni for your excellent work!
