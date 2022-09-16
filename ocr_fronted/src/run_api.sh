#!/bin/sh
# cd /home/project/ocr_vue_django/ocr_front/
# npm install
# npm run pre_dev


sed -i 's/user  nginx/user  root/g' /etc/nginx/nginx.conf

if [ -f "/etc/nginx/conf.d/vue.conf" ]
then
      rm -rf /etc/nginx/conf.d/vue.conf
else
      echo "This file is not exist."
fi

# if [[ $# -ge 1 ]]; then
#     if [[ $1 != 'pro' ]] && [[ $1 != 'pre' ]] && [[ $1 != 'test' ]]; then
#         echo 'usage: ./run_api.sh [pro|pre|test]'
#     fi
#     if [[ $1 == 'pre' ]]; then
#         backend=http://wan-backend-service
#     fi
#     if [[ $1 == 'pro' ]]; then
#         backend=http://wan-backend-service
#     fi
# fi


cat >> /etc/nginx/conf.d/vue.conf <<EOF
server {
    listen       80;
    server_name  localhost;

    charset utf-8;

    location / {
        root   /app/dist/;
         try_files tempuri tempuri/ /index.html last;
        index  index.html;
    }


    location /api/ {
        proxy_pass   http://36.111.131.226:8000;
        proxy_set_header   Host             temphost;
        proxy_set_header   X-Real-IP        tempremote_addr;
        proxy_set_header   X-Forwarded-For  tempproxy_add_x_forwarded_for;
    }
}
EOF

sed -i 's/temp/$/g' /etc/nginx/conf.d/vue.conf
service nginx stop
nginx -g "daemon off;"

echo "===================config Permission==================="
chmod 775 /home/project/ocr_vue_django/ocr_front/run_api.sh