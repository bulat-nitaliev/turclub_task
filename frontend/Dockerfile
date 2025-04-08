FROM node:14-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build
RUN npm run generate
EXPOSE 3000

CMD ["npm", "run", "start"]