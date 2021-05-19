FROM node:slim
WORKDIR /app
COPY . /app
RUN npm install -g express-generator
RUN npm install express --save
EXPOSE 3000
CMD node app.js