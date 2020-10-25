FROM nginx:latest

RUN mkdir -p /static
#не создаем папку media, при развертывании контейнера папка создается атвоматически

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

WORKDIR /static
RUN chown -R nginx:nginx /static

WORKDIR /media
RUN chown -R nginx:nginx /media