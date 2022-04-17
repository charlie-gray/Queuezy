# syntax=docker/dockerfile:1
FROM mysql
# WARNING, REPLACE DEFAULT MYSQL PASSWORD BELOW
ENV MYSQL_ROOT_PASSWORD=toor 
EXPOSE 3306

# A Dockerfile is also provided her if you would like to make manual configurations to the SQL server
# NOTE: The "startDocker.sh" file is not effected by this config. You must launch this Dockerfile manually