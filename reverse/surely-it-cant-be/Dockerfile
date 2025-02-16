FROM node:22

WORKDIR /app
COPY ./infra /app
COPY ./client/dist/app /app/innocent-binary
COPY ./trade-secrets.jpg /root/trade-secrets.jpg

CMD ["node", "main.js"]
