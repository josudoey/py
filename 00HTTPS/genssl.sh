#!/bin/bash
ssh-keygen -t rsa -b 2048 -P '' -f ./ssl.key
openssl req -key ./ssl.key -new -x509 -days 7300 -sha256 -extensions v3_ca  -out ssl.cert
