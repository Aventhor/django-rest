```sh
$ cp .env.example .env
$ docker-compose up -d
$ pipenv shell
$ pipenv install
$ python backend/manage.py makemigrations
$ python backend/manage.py migrate
$ python backend/manage.py createsuperuser
$ python backend/manage.py runserver
```