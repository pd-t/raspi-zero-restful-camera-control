#!/bin/sh

# Install packages
apt-get update \
    && apt-get install --no-install-recommends -y python3 python3-opencv pip \
    && apt-get autoclean

# Get Sources
git clone https://github.com/pd-t/raspi-zero-fastapi-camera-control.git

# Install Sources
mkdir -p /opt/camera-control
cp -r raspi-zero-fastapi-camera-control/  /opt/camera-control

# Create Start-Up Script
cp raspi-zero-fastapi-camera-control/init.sh /etc/init.d/camera-control.sh
sudo chmod +x /etc/init.d/camera-control.sh
sudo chown root:root /etc/init.d/camera-control.sh
sudo update-rc.d camera-control.sh defaults
sudo update-rc.d camera-control.sh enable

# Clean Up
rm -r raspi-zero-fastapi-camera-control

# pip3 install poetry
# poetry config virtualenvs.create false &&  poetry install --no-dev --no-interaction --no-ansi

pip3 install fastapi==0.75.1 gunicorn==20.1.0

modprobe bcm2835-v4l2

shotdown -r now
