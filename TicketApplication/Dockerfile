FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
COPY . .

EXPOSE 8050

CMD [ "python3", "-m" , "flask", "run", "--host=localhost"]