FROM tiangolo/uvicorn-gunicorn:python3.8

ENV TZ America/Sao_Paulo

RUN apt-get update
RUN apt-get -y upgrade

# Driver p/ Selenium
RUN apt install -y chromium=90.0.4430.212-1~deb10u1

# Python configuration ###################################################################
WORKDIR  /usr/src/app
ENV PYTHONPATH /usr/src/app
ENV PYTHONHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./scripts/dev-configure-python.sh ./scripts/dev-configure-python.sh
COPY poetry.lock pyproject.toml ./

RUN chmod a+x ./scripts/dev-configure-python.sh
RUN ./scripts/dev-configure-python.sh
##########################################################################################

COPY ./ ./

RUN cat ./scripts/start-reload.sh > /start-reload.sh
CMD ["bash", "/start-reload.sh"]