FROM imiell/taigaio:latest
MAINTAINER tubia <tubia@hacari.net>

ADD local.py /home/taiga/taiga-back/settings/local.py
ADD main.json /home/taiga/taiga-front/conf/main.json
