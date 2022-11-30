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