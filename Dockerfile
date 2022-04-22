FROM debian:bullseye as python-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y python3 python3-opencv pip \
    && apt-get autoclean

FROM python-base as builder-base

RUN pip3 install poetry==1.1.4
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false &&  poetry install --no-dev --no-interaction --no-ansi


FROM builder-base AS app
ENV PROJECT_DIR="/app"
ENV WEB_CONCURRENCY=1

COPY gunicorn_conf.py $PROJECT_DIR/

WORKDIR $PROJECT_DIR

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY src $PROJECT_DIR/src

EXPOSE 8000
ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD [ "gunicorn", "--worker-class uvicorn.workers.UvicornWorker", "--config ./gunicorn_conf.py", "--chdir src", "src.main:app"]
