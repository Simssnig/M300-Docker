# Docker-Compose Cluster with Grafana, InfluxDB, and Telegraf
This guide will show you how to configure and start a Docker-Compose cluster running Grafana, InfluxDB, and Telegraf.
## Introduction
This is just a lab version, tested with telegraf:1.25.0, influxdb:2.6.1
## Clone the repository
```
git clone https://github.com/Simssnig/M300-Docker.git
```
Tested with telegraf:1.25.0, influxdb:2.6.1
## Install Docker and docker-compose
```
apt-get install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
### Add current user to Docker group for simplicity
```
sudo usermod -aG docker < aktuellen Benutzenamen >
```
Log out and log back in after this step.

### Install dependencies
```
sudo apt-get install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt-get install -y python3 python3-pip
sudo pip3 install docker-compose
```
### Enable autostart of Docker daemon
```
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```
## Setup
1. clone this repository
```
git clone https://github.com/Simssnig/M300-Docker.git
```
All necessary environment and init variables are described in the .env file.

The following command can generate a 32-bit hex code that is used as an access token in the .env file (the variable is: DOCKER_INFLUXDB_INIT_ADMIN_TOKEN)

!! IMPORTANT: This key has to be generated (with the command below) and placed (manualy copy and paste) inside the .env file.
```
openssl rand -hex 32
```
2. Navigate to the cloned repository and start the services using Docker Compose
```
cd M300-Docker
docker-compose up -d
```
## Connecting the Services
1. Grafana is available at http://localhost:3000 with default credentials admin/admin.
2. InfluxDB is available at http://localhost:8086 with the credentials admin/sml12345.
3. Telegraf is already configured to collect metrics and send them to InfluxDB.
## Additional Configuration
### Retrieve Influx query
https://docs.influxdata.com/influxdb/cloud/query-data/execute-queries/data-explorer/
### Connect to Grafana
https://www.stackhero.io/en/services/Grafana/documentations/Getting-started/How-to-connect-Grafana-to-InfluxDB-v2

If following the instructions from the link above, replace http://localhost:8086 with http://influxdb:8086. All variables are in the .env file.
### Create Grafana dashboards
https://grafana.com/docs/grafana/latest/dashboards/
## Handling the containers
You can configure Grafana, InfluxDB, and Telegraf to your needs by modifying the respective configuration files

After modifying the configurations, restart the services to apply the changes.
### Shutting Down
To stop the services and remove the containers, run the following command:
```
docker-compose down
```
