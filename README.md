# prombot

## Description

Converts alerts sent by prometheus to text message and send them to a telegram

Example message:

```
{config.MESSAGE_PREFIX} firing: <alert 1 summary>, <alert 2 summary>

firing(link to alert): <alert 1 description>
firing(link to alert): <alert 2 description>
```


## Local Installation

```sh
virtualenv pyvenv
git clone xxx
cd xxx
pip install .
pyvenv/bin/prombot
```

Configure config.py, especially the telegram bot part
## Docker

### Build

```sh
docker build -t prombot .
```

### Run

Create a local copy and configure config.py (i.e. in /home/docker/config.py), especially the telegram bot part.

```sh
docker pull vche/prombot
docker run -p 9087:9087 -v /home/docker/config.py:/prombot/config.py prombot
```

### Docker compose

```yaml
  prombot:
    container_name: prombot
    image: vche/prombot
    ports:
      - 9087:9087
    volumes:
      - /home/docker/config.py:/prombot/config.py
```
