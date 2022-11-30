# wakeup-machine
call line bot app for scheduler

# step

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
(.env) $ pip install apscheduler #install apscheduler
```

## docker

```shell
sudo su
docker build -t wakeup-machine . --no-cache
docker run --name wakeup -e URL=https://yourwebsite.domain.com/ wakeup-machine
```

### docker examples


#### without-log
```shell
docker run -d \
--restart always \
--name wakeup-render \
-e URL=https://yourwebsite.domain.com/ \
wakeup-machine
```

```-e URL=???``` ??? 輸入你要被呼叫的網址

#### with-log

```shell
docker run -d \
--restart always \
--name wakeup-render \
-e URL=https://yourwebsite.domain.com/ \
-v /home/yen/wakeup-machine:/app \
wakeup-machine
```

```-v``` 請輸入當前目錄, 例如我的是 ```/home/yen/wakeup-machine```

不知道怎麼查看當前目錄，可以輸入 ```pwd```