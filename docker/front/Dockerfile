FROM node:17

LABEL version="1.0"
LABEL org.opencontainers.image.authors="Carlos Guillermo Jimenez Salcedo"

WORKDIR /usr/src/git_manager_front

ENV PATH /app/node_modules/.bin:$PATH

COPY ./front/package*.json ./
RUN npm install

COPY ./front ./

CMD ["npm", "start"]
