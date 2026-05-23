FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Раздаем собранную статику через легковесный сервер alpine
FROM alpine:latest
RUN apk add --no-cache static-server
WORKDIR /app
COPY --from=build /app/build ./
CMD ["static-server", "-p", "3000"]