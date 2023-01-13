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
