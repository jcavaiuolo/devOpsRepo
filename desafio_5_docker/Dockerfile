FROM node:18-alpine 
# aunque en un escenario real habría que confirmar la versión de node.js compatible

WORKDIR /app 
# todas las operaciones que se realicen después de esta instrucción se ejecutarán dentro de /app

COPY /app-template-nestjs/* . 
# Copiamos todo el código de la app al contenedor. caso de poner el Dockerfile en el mismo directorio que el codigo usar la siguiente linea
# COPY . . 

RUN npm install 
# el archivo package.json y package-lock.json tiene dependencias

RUN npm run build 
# build de la app Next.js

EXPOSE 3000 
# Exponemos el puerto en el que corre la app

CMD ["npm", "run", "start"] 
# Comando por defecto para iniciar la app
