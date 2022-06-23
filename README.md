# Raspi Zero FastAPI Camera Control

The project should make it possible to control a Pi Camera connected via 
CSI to a Raspi Zero W using a REST service. The REST service can be 
accessed via a Wi-Fi hotspot.

The following recording features are implemented:
- Single Image
- Video (start/stop)

The project is based on the idea of an independent companion computer for 
drones for imaging with special cameras (e.g. a [NOIR Pi Camera]
[NOIRPiCamera]). For more information why we need this type of camera, see 
[here][NDVI].

[NOIRPiCamera]: https://www.raspberrypi.com/products/pi-noir-camera-v2/
[NDVI]: https://www.raspberrypi.com/news/whats-that-blue-thing-doing-here/


## Installation
Start from a fresh new Raspberry Pi OS Lite (the following steps where 
tested using this [version][RaspiOSLite]). Connect it with your WiFi and 
login using ssh (this can be prepared using the [imager][RaspberryPiImager]).

[RaspiOSLite]: https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2022-04-07/

[RaspberryPiImager]: https://www.raspberrypi.com/software/

Connect the Camera to your Raspberry and login via ssh to activate your Pi 
Camera as described [here][PiCameraInstall]. Be aware that you need a 
special CSI cable for the Pi Zero. In case your images appear red, 
append `awb_auto_is_greyworld=1` to the end of `/boot/config.txt`. In 
addition to this you have to increase the gpu memory to 256MB for full 
resolution images, see the performance options in `raspi-config`.

[PiCameraInstall]: https://www.raspberrypi.com/documentation/accessories/camera.html

The following command installs the FastAPI REST service and the automatic 
start up scripts.
```
curl -sSL https://raw.githubusercontent.com/pd-t/raspi-zero-fastapi-camera-control/main/install.sh | sudo sh
```
After reboot the REST service is available under 
`http://RASPI_ZERO_IP:8000/docs`. The images and videos are saved to 
`/camera` on the Raspberry Pi.

As mentioned before, the original idea was to provide a REST service for 
drone companion computers far away from given Wi-Fi infrastructure. 
In order to still have access to the REST service under these circumstances,
a hotspot can be activated. Just execute the following command:

```
curl -sSL https://raw.githubusercontent.com/pd-t/raspi-zero-fastapi-camera-control/main/hotspot/setup.sh | sudo sh
```

Afterwards, connect to `CameraControl` network using the password 
`CameraControl`. This makes REST service available at `http://192.168.4.
1:8000/docs`.

## Development

Feel free to adapt this code to your project. There is a 
[poetry](https://python-poetry.org/) environment provided which can be 
activated using

```
poetry install
poetry shell
```

Afterwards, you can run the FastAPI code with

```
PYTHONPATH="." python src/run.py
```

and access the docs at `http://localhost:8000/docs`.

### Update FastAPI using OpenAPI

An almost working base for the API can be generated the OpenAPI 
specification:

```
fastapi-codegen --input oas/openapi.yaml -t jinja --output src
```

### Docker

Last but not least for isolated testing a docker version is provided.

```
docker-compose up app
```

On a capable system like the Raspberry Pi version 3 or 4, it is definitely 
an option to deploy the application using docker. Remember to add the 
`restart: always` flag to the docker-compose script.

## License

This project under the terms of both the MIT license. 

See [LICENSE](LICENSE) for details.
