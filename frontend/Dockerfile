FROM node:18-alpine

WORKDIR /app

# Instalar Ionic CLI globalmente
RUN npm install -g @ionic/cli

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código
COPY . .

# Puerto para desarrollo
EXPOSE 8100

# Comando para desarrollo
CMD ["ionic", "serve", "--external"]