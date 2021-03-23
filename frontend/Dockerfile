FROM node:15.12

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY package.json package-lock.json /frontend/
RUN npm install

COPY . /frontend/
