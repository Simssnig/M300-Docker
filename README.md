# M300-Docker
## Introduction
This is just a lab version.

## Clone the repository
```
git clone https://github.com/Simssnig/M300-Docker.git
```
Tested with telegraf:1.25.0, influxdb:2.6.1
## Install Docker
```
apt-get install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
## Add current user to Docker group for simplicity
```
sudo usermod -aG docker < aktuellen Benutzenamen >
```
Log out and log back in after this step.

## Install dependencies
```
sudo apt-get install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt-get install -y python3 python3-pip
sudo pip3 install docker-compose
```
## Enable autostart of Docker daemon
```
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```
## Configuration
All necessary environment and init variables are described in the .env file.

The following command can generate a 32-bit hex code that is used as an access token in the .env file (the variable is: DOCKER_INFLUXDB_INIT_ADMIN_TOKEN)

!! IMPORTANT: This key has to be generated (with the command below) and placed (manualy copy and paste) inside the .env file.
```
openssl rand -hex 32
```
## Start Docker
In the project folder, run:
```
docker-compose up -d
```
## Retrieve Influx query
https://docs.influxdata.com/influxdb/cloud/query-data/execute-queries/data-explorer/
## Connect to Grafana
https://www.stackhero.io/en/services/Grafana/documentations/Getting-started/How-to-connect-Grafana-to-InfluxDB-v2

If following the instructions from the link above, replace http://localhost:8086 with http://influxdb:8086. All variables are in the .env file.
## Create Grafana dashboards
https://grafana.com/docs/grafana/latest/dashboards/
