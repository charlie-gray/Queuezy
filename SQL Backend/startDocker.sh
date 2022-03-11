#!/bin/bash

echo Set root password: 
read pass

docker run --name=PeopleCounterSQL -p 3306:3306 -e MYSQL_ROOT_PASSWORD=$pass -d mysql           
