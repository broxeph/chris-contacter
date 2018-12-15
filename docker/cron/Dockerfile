FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/

# Install cron
RUN apt-get update
RUN apt-get -y install -qq cron

# Setup cron job
RUN (echo "* * * * * python manage.py update_conversations > /proc/1/fd/1 2> /proc/1/fd/2") | crontab

# Run the command on container startup
CMD ["cron", "-f"]
