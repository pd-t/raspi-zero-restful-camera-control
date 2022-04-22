#! /bin/sh

### BEGIN INIT INFO
# Provides:          camera-control
# Required-Start:
# Required-Stop:
# Should-Stop:
# Default-Start:     3 5
# Default-Stop:
# Short-Description: Start FastAPI Camera Control.
### END INIT INFO

case "$1" in
 start)
 CAMERA_DATA_PATH="/camera"
 mkdir -p $CAMERA_DATA_PATH
 WEB_CONCURRENCY=1 gunicorn --worker-class uvicorn.workers.UvicornWorker --config ./gunicorn_conf.py --chdir /opt/camera-control src.main:app
 ;;
esac

exit 0