# Этап 1: Сборка проекта
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Этап 2: Подготовка статики
FROM alpine:latest
WORKDIR /app
# Просто копируем результат сборки из первого этапа в текущий контейнер
COPY --from=build /app/build ./build