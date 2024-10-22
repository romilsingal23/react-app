#!/bin/sh

# Replace placeholders with actual environment variables
envsubst < /usr/share/nginx/html/env.template.js > /usr/share/nginx/html/env.js

# Start NGINX
nginx -g 'daemon off;'
