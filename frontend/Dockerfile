FROM node:18-alpine

WORKDIR /app

# Install Ionic CLI globally
RUN npm install -g @ionic/cli

COPY package*.json ./


RUN npm install


COPY . .

EXPOSE 8100

ENV CHOKIDAR_USEPOLLING=true
ENV WATCHPACK_POLLING=true

# Use --host 0.0.0.0 for Docker and --poll for file watching
CMD ["ionic", "serve", "--host", "0.0.0.0", "--poll", "1000"]