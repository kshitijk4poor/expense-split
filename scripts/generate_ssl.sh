#!/bin/bash

# Create SSL directory
mkdir -p api-gateway/config/ssl

# Generate self-signed SSL certificates
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout api-gateway/config/ssl/server.key \
    -out api-gateway/config/ssl/server.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/OU=OrgUnit/CN=localhost"