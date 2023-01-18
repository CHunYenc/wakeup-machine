# wakeup-machine

This program will wake up the sleeping machine.

這個程式主要把睡眠的機器喚醒。

- [wakeup-machine](#wakeup-machine)
- [docker](#docker)
  - [with-log](#with-log)
- [docker-compose](#docker-compose)
- [development](#development)
  - [Virtual Environment](#virtual-environment)
  - [pip install](#pip-install)
  - [.env and environment variables](#env-and-environment-variables)

# docker

## with-log

```shell
docker run -d \
--restart always \
--name wakeup-render \
-e URL=https://yourwebsite.domain.com/ \
-e APSCHEDULER_MINUTE=*/10 \
-v /home/yen/wakeup-machine:/app \
chunyenc/wakeup-machine
```

```-e URL=???``` ??? 輸入你要被呼叫的網址

```-v``` 請輸入當前目錄, 例如我的是 ```/home/yen/wakeup-machine```

不知道怎麼查看當前目錄，可以輸入 ```pwd```

# docker-compose

```
version: '3.9'

services:
  service-one:
    image: chunyenc/wakeup-machine
    environment:
      - URL=https://example.com
      - APSCHEDULER_MINUTE=*/10
      - APSCHEDULER_HOUR=0-1,5-23
      - APSCHEDULER_DAY_OF_WEEK=mon-fri
    volumes:
      - ./pricing.log:/app/scheduler.log

  service-two:
    image: chunyenc/wakeup-machine
    environment:
      - URL=https://example.com
      - APSCHEDULER_MINUTE=*/10
      - APSCHEDULER_HOUR=9-23
    volumes:
      - ./linebot.log:/app/scheduler.log
```

# development

## Virtual Environment

[Virtual Environment](https://docs.python.org/3/tutorial/venv.html)

```shell
# Ubuntu
python3 -m venv .env #create env
source .env/bin/activate #run env
```

## pip install

```
(.env) $ pip install -U pip #update pip
(.env) $ pip install apscheduler # install apscheduler
```

## .env and environment variables

```dotenv
URL=??
APSCHEDULER_YEAR=??
APSCHEDULER_MONTH=??
APSCHEDULER_DAY=??
APSCHEDULER_WEEK=??
APSCHEDULER_DAY_OF_WEEK=??
APSCHEDULER_HOUR=??
APSCHEDULER_MINUTE=??
APSCHEDULER_SECOND=??
```
