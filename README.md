Chris Contacter
===============

For those times when manually sending Hangouts chats, emails and texts simply gets too tedious...

Chris Contacter will attempt to send a message via email, then will send a text.
It will wait an hour between each service, and stop when it receives a response.

This is meant to be run locally, and is not production-ready; hence unforgivable things like running Postgres in Docker, and Celery with `DEBUG = True`.

Stack
-----

- Python 3.6 (Celery 4.2 isn't compatible with Python 3.7 due to use of `async` keyword)
- Docker
- Postgres
- Django
- Bootstrap 4

Setup
---

(Ubuntu 18.10)

1. `sudo apt install apt-transport-https ca-certificates curl software-properties-common`
2. `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
3. `sudo apt install docker-ce docker-compose`
4. `sudo usermod -a -G docker $USER`
5. `sudo systemctl restart docker`
6. `sudo chmod 666 /var/run/docker.sock`
7. Copy `chris_contacter/secrets.py.template` to `chris_contacter/secrets.py` and fill in credentials 
8. `docker-compose build`
9. `docker-compose run web python manage.py migrate --rm`
10. `docker-compose run web python manage.py createsuperuser --rm`

Run
---

- `docker-compose up`

Shell
-----

- `docker-compose run web python manage.py shell`

TODO
----

- Write tests
- Connect email API
- Connect text API
