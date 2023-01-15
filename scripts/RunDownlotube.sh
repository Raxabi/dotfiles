#!/bin/bash

: '

Automatically set-up the downlotube server and downlotube client process.

If already these processes exists in a screen process it stop the script exiting with a statud code of 0 (all correct)

'

server=$(screen -ls | grep server)
client=$(screen -ls | grep  client)
#discord=$(screen -ls | grep discord)

if [[ $server != "" ]] || [[ $client != "" ]]; then
  echo "Ya hay sesiones en funcionamiento"
  exit 0
else
  # Para la seseion del servidor de Downlotube
  echo "Creando la sesion de servidor de Downlotube"
  sleep 0.5
  screen -dmS "server" bash -c "cd ~/downlotube/server/ && source Flask_Downloader/bin/activate && gunicorn --timeout 120 -w 6 -b 192.168.1.59:5000 main:app"
  # Para la sesion de react para Downlotube
  echo "Creando la sesion frontend de Downlotube"
  sleep 0.5
  screen -dmS "client" bash -c "cd ~/downlotube/client/ && npm run preview"
  : '
  echo "Creando la sesion de Discord"
  sleep 0.5
  screen -dmS "discord" bash -c "cd ~/Tito-Bot/ && source Discord_Bot/bin/activate && python main.py"
  '
fi