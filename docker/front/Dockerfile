FROM node:17

LABEL version="1.0"
LABEL org.opencontainers.image.authors="Carlos Guillermo Jimenez Salcedo"

WORKDIR /usr/src/
COPY ./front/package.json ./
RUN npm install
ENV PATH /usr/src/node_modules/.bin:$PATH

WORKDIR /usr/src/git_manager_front
COPY ./front ./

CMD ["npm", "start"]
