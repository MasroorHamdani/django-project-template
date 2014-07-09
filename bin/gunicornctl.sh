#!/bin/sh

# Specify path variable
PATH=/sbin:/usr/sbin:/bin:/usr/bin

# Kill me on all errors
set -e

case "$1" in
  start)
    /home/hasher/project/django-project/django-project-template/bin/gunicorn_django -D \
        -w 4 \
        -p /tmp/django_todo.pid \
        --log-file=//tmp/django_todo.log \
        -b 127.0.0.1:8000 \
        django_todo.dev_settings
    ;;
  stop)
    kill `cat /tmp/django_todo.pid`
    ;;    
  *)
    echo "Usage: $0 {start|stop}"
    exit 1
    ;;
esac
