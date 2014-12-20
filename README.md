# Accollo
A minimalistic taiga.io docker image easily configurable.

## What it does
This Docker image is totally based on [this one](https://registry.hub.docker.com/u/imiell/taigaio/) by @imiell but it adds the possibility to configure some settings for the taiga backend and frontend.

## How to use it
Simply `git clone` this repo.
Then edit `local.py` for backend settings and `main.json` for frontend settings.
```
cd accollo
```
Build it with Docker:
```
docker build -t accollo
```
To run it and daemonize the process:
```
docker run -d -p 8000:8000 -p 8001:8001 accollo /bin/bash -c '/root/start_postgres.sh && /root/start_taiga.sh && echo READY! && sleep infinity'
```

## Default
The default settings are set to prevent registration.

## Further development
Add persistence, saving in a volume postgres data.

## Credits
All the credits goes firstly to the [taiga.io](https://github.com/taigaio/) team and to @imiell that created the docker image on which this one is based.