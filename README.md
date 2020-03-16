# prombot

## Description

Converts alerts sent by prometheus to text message and send them to a telegram bot

## Installation

```sh
virtualenv pyvenv
git clone xxx
cd xxx
pip install .
pyvenv/bin/prombot
```

## Docker

### Build

```sh
docker build -t prombot .
```

### Run

```sh
docker run -p 9087:9087 prombot -v /opt/config.py:/prombot/config.py
```

### Docker compose

```sh
docker run -p 9087:9087 prombot -v /opt/config.py:/prombot/config.py
```
