FROM node:alpine

WORKDIR /frontend

COPY package*.json .

RUN npm install

COPY . .

CMD [ "npm","run","start" ]