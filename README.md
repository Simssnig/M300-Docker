# M300-Docker
## docker installieren
```
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
alle notwendigen umgebungs und init variablen werden im file configuration.conf beschrieben

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
