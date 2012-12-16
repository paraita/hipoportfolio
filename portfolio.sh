#!/bin/bash
set -e
LOGFILE=/home/paraita/www-dir/portfolio/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=paraita
GROUP=paraita
ADDRESS=0.0.0.0:8001
cd /home/paraita/www-dir/portfolio
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS --bind=$ADDRESS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE