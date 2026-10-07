#!/bin/sh
# пак бэкап: дамп именованных томов compose в один tar
set -e
OUT="backup-$(date +%F).tar.gz"
docker run --rm -v p4-devops-nginx_data:/data -v "$PWD":/out alpine tar czf "/out/$OUT" /data
echo "saved $OUT"
