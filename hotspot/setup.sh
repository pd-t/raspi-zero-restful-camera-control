#!/bin/sh

apt-get update \
    && apt-get install --no-install-recommends -y hostapd dnsmasq \
    && apt-get autoclean

curl -sSL https://raw.githubusercontent.com/pd-t/raspi-zero-fastapi-camera-control/main/hotspot/dhcpcd.conf > /etc/dhcpcd.conf
curl -sSL https://raw.githubusercontent.com/pd-t/raspi-zero-fastapi-camera-control/main/hotspot/dnsmasq.conf > /etc/dhcpcd.conf
curl -sSL https://raw.githubusercontent.com/pd-t/raspi-zero-fastapi-camera-control/main/hotspot/hostapd.conf > /etc/hostapd/hostapd.conf

rfkill unblock wlan
systemctl unmask hostapd
systemctl enable hostapd
systemctl reboot