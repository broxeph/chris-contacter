Chris Contacter
===============

For those times when manually sending Hangouts chats, emails and texts simply gets too tedious...

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
8. `docker-compose run web python manage.py createsuperuser`

Run
---

- `docker-compose up`
