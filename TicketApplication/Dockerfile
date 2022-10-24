FROM python:3.8
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install --no-cache-dir -r /var/www/requirements.txt
COPY . .

EXPOSE 8050

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8050"]