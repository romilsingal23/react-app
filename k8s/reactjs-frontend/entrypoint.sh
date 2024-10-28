#!/bin/sh

# Debugging log to check if REACT_APP_BACKEND_URL is set
echo "REACT_APP_BACKEND_URL is set to: $REACT_APP_BACKEND_URL"
# Replace placeholders with actual environment variables
envsubst < /usr/share/nginx/html/env.template.js > /usr/share/nginx/html/env.js
#cp /usr/share/nginx/html/env.template.js /usr/share/nginx/html/env.js
echo "env.js content after substitution:"
cat /usr/share/nginx/html/env.js
# Start NGINX
nginx -g 'daemon off;'
