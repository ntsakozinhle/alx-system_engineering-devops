#!/usr/bin/env bash

# MySQL commands to create user and grant permissions
mysql -u root -p <<EOF
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrect280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
EOF
