#!/bin/sh

# install necessary packages
apt-get update \
    && apt-get install --no-install-recommends -y python3 python3-opencv pip git \
    && apt-get autoclean

# download git repo
git clone https://github.com/pd-t/raspi-zero-fastapi-camera-control.git

# install necessary sources and config files
mkdir -p /opt/camera-control
cp -r raspi-zero-fastapi-camera-control/src  /opt/camera-control
cp raspi-zero-fastapi-camera-control/config.cfg   /opt/camera-control
cp raspi-zero-fastapi-camera-control/gunicorn_conf.py   /opt/camera-control

# register start-up script at init.d
cp raspi-zero-fastapi-camera-control/init.sh /etc/init.d/camera-control.sh
sudo chmod +x /etc/init.d/camera-control.sh
sudo chown root:root /etc/init.d/camera-control.sh
sudo update-rc.d camera-control.sh defaults

# remove downloaded sources
rm -r raspi-zero-fastapi-camera-control

# install fastapi components
pip3 install fastapi==0.75.1 gunicorn==20.1.0 uvicorn==0.17.6

# make raspi camera available for cv2.VideoCapture after reboot
modprobe bcm2835-v4l2
reboot
