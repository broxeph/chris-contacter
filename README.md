Chris Contacter
===============

For those times when manually sending Hangouts chats, emails and texts simply gets too tedious...

Chris Contacter will attempt to send a message via Hangouts chat, then email, then text, then phone call.
It will wait an hour between each medium, and stop when it receives a response.

This is meant to be run locally, and is not production-ready; hence unforgivable things like running Celery with `DEBUG = True`.

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
7. `docker-compose build`
8. `docker-compose run web python manage.py migrate --rm`
9. `docker-compose run web python manage.py createsuperuser --rm`

Run
---

- `docker-compose up`

TODO
----

- Write tests
- Connect chat API
- Connect email API
- Connect text API
- Connect call API
