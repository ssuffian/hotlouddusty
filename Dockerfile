FROM python:3.6.4

RUN set -ex && pip install pipenv --upgrade

RUN apt-get update && apt-get install -yqq portaudio19-dev python-dev alsa-utils libav-tools

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN set -ex && pipenv install --system --deploy --dev

COPY hotlouddusty/ /app/hotlouddusty/
COPY lib/ /usr/local/lib/
RUN set -ex && cd /usr/local/lib/py-sds011 && python setup.py install
#RUN set -ex && pip install -e /app

WORKDIR /app/hotlouddusty
EXPOSE 20175
