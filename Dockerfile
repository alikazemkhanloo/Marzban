FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update \
    && apt-get install -y curl unzip gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

# RUN curl -L https://github.com/Gozargah/Marzban-scripts/raw/master/install_latest_xray.sh | bash

COPY ./xray-core/xray /usr/local/bin/
COPY ./xray-core/geo* /usr/local/share/xray/

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get remove -y curl unzip gcc python3-dev

CMD ["bash", "-c", "alembic upgrade head; python main.py"]