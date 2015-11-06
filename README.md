# WebTasks

## Quick Start

### Download sources

```sh
apt-get install git python-virtualenv
```

```sh
$ git clone https://github.com/Kaniabi/webtasks.git

$ cd webstasks
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt

```

### Set Environment Variables

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

### Testing

Without coverage:

```sh
$ export APP_SETTINGS="project.config.TestingConfig"
$ python manage.py test
```

With coverage:

```sh
$ export APP_SETTINGS="project.config.TestingConfig"
$ python manage.py cov
```
