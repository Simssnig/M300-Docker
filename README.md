# M300-Docker
## docker installieren
```
apt-get install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
## der einfachheit halber den aktuellen benutzer zur docker gruppe hinzufügen
```
sudo usermod -aG docker < aktuellen Benutzenamen >
```
danach wieder kurz aus- und einloggen
## abhängigkeiten installieren
```
sudo apt-get install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt-get install -y python3 python3-pip
sudo pip3 install docker-compose
```
## autostart des docker daemon aktivieren
```
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```
## konfiguration
alle notwendigen umgebungs und init variablen werden im file .env beschrieben

mit folgendem befehl kann ein 32bit hex code generiert werden
dieser wird als access token eingesetzt (DOCKER_INFLUXDB_INIT_ADMIN_TOKEN)
```
openssl rand -hex 32
```
## docker starten
im ordner vom git projekt
```
docker-compose up -d
```
## influx query heraussuchen
https://docs.influxdata.com/influxdb/cloud/query-data/execute-queries/data-explorer/
## grafana verbinden
anstelle von http://localhost:8086 http://influxdb:8086 verwenden 

https://www.stackhero.io/en/services/Grafana/documentations/Getting-started/How-to-connect-Grafana-to-InfluxDB-v2
alle variablen befinden sich im .env file
## grafana dashboards anlegen
https://grafana.com/docs/grafana/latest/dashboards/
