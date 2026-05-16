Simple program to fetch weather every 10 minute and log it in to a file
(requests module + linux systemd service).

created script `weather_program.sh`
and also weather.service/weather.timer to run the program every 10 minute.

`cat /etc/systemd/system/Weather.service`
```
[Unit]
Description=Program that fetches weather from website
After=network-online.target

[Service]
ExecStart=/usr/bin/python3 /home/nikol/weatherprogram/weather_program.sh
WorkingDirectory=/home/nikol/weatherprogram
User=nikol
Restart=on-failure  

[Install]
WantedBy=multi-user.target
```

this service need the timer to run every 10 minute 
`cat /etc/systemd/system/weather.timer`

```
[Unit]
Description=run the weather_program.sh every 10 minute and fetch the weather

[Timer]
OnUnitActiveSec=10min
Unit=weather.service

[Install]
WantedBy=timers.target
```

then we force enable the timer service and it starts to run every 10 min and log the weather in `weather_log.txt`
