#!/bin/bash

docker stop odjemalec
docker stop streznik

docker rm streznik
docker rm odjemalec


docker network create omrezje


docker build -t server ./server
docker build -t client ./client

docker run --privileged -d --network omrezje --name streznik -p 3000:3000 server 
docker run -d --network omrezje --name odjemalec -p 3001:3001 client 

ip_address=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' odjemalec)
ip_address2=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' streznik)

echo "Odjemalec ip: $ip_address:3001"
echo "SErver ip: $ip_address2:3000"