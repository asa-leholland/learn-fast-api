#!/bin/bash
# This is just a shortcut when developing locally to rebuild image if given docker issues
# execute using "bash rebuild-docker.sh"
# sudo docker-compose -f docker-compose.yml down --remove-orphans
# sudo docker-compose -f docker-compose.yml build
# sudo docker-compose -f docker-compose.yml up -d


docker-compose -f docker-compose.yml down --remove-orphans
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d