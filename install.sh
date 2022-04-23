#!/bin/sh

# install packages
apt-get update \
    && apt-get install --no-install-recommends -y python3 python3-opencv pip \
    && apt-get autoclean

# get sources
git clone https://github.com/pd-t/raspi-zero-fastapi-camera-control.git

# install sources
mkdir -p /opt/camera-control
cp -r raspi-zero-fastapi-camera-control/  /opt/camera-control

# create start-up script
cp raspi-zero-fastapi-camera-control/init.sh /etc/init.d/camera-control.sh
sudo chmod +x /etc/init.d/camera-control.sh
sudo chown root:root /etc/init.d/camera-control.sh
sudo update-rc.d camera-control.sh defaults

# remove downloaded sources
rm -r raspi-zero-fastapi-camera-control

# install fastapi components
pip3 install fastapi==0.75.1 gunicorn==20.1.0

# make raspi camera available for cv2.VideoCapture after reboot
modprobe bcm2835-v4l2
reboot
