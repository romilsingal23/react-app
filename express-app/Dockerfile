# Stage 1: Builder stage
FROM node:18-alpine as builder

# Set environment to production for optimized builds
ENV NODE_ENV=production

# Create a non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Copy only package.json and package-lock.json (or yarn.lock) to leverage Docker's layer caching
COPY package*.json ./

# Install only production dependencies for smaller image
RUN npm install --only=production

# Copy the rest of the application code
COPY . .

# Stage 2: Final stage
FROM node:18-alpine

# Set environment to production
ENV NODE_ENV=production

# Create a non-root user in the final stage for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Copy over the app from the builder stage
COPY --from=builder /app /app

# Ensure the application runs with non-root privileges for security
USER appuser

# Expose the port the application will run on
ENV PORT 8080
EXPOSE 8080

# Start the application
CMD ["npm", "start"]

