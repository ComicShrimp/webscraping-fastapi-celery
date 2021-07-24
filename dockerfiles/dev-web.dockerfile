FROM tiangolo/uvicorn-gunicorn:python3.8-slim

ENV TZ America/Sao_Paulo

RUN apt-get update
RUN apt-get -y upgrade

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