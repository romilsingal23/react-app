# Step 1: Build the React app
FROM node:16-alpine as build
WORKDIR /app

COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

# Step 2: Serve the React app with NGINX
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Copy the env.template.js to the NGINX folder
COPY ./public/env.template.js /usr/share/nginx/html/env.template.js

# Add entrypoint script to dynamically substitute the environment variable
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80

# Use the entrypoint script to substitute variables before starting NGINX
CMD ["/entrypoint.sh"]
