#grab nginx image
FROM alpine:3.12.2

#update package cache
RUN apk update

#install nginx
RUN apk add nginx

#make directories needed for nginx
RUN mkdir -p /run/nginx

RUN mkdir -p /var/www/html/admin

#drop config to make things work
COPY nginx/gamification.conf /etc/nginx/conf.d/

#copy over static assets
COPY cyberpi_dress_up_game/media /var/www/html

COPY nginx/admin/ /var/www/html/admin

#expose port 80
EXPOSE 80

#run nginx until the end of time
CMD nginx && while true; do sleep 12 ; done

