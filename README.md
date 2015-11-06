# WebTasks



## Configuring

### Configure the environment.

This configuration is based on an empty Ubuntu vagrant box, more speficially, the box "phusion/ubuntu-14.04-amd64".

```sh
$ apt-get install git python3-pip npm nodejs
$ ln -s /usr/bin/nodejs /usr/bin/node
$ pip3 virtualenv
$ npm install -g http-server
```

### Download the sources

```sh
$ git clone https://github.com/Kaniabi/webtasks.git
```

### Create the server environment using virtualenv

The environment must be created only once.

```sh
$ cd webstasks
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py create_db
$ deactivate
```


## Executing

### Start the server

The server will be available at http://localhost:5000.

```sh
$ cd webtasks
$ source .venv/bin/activate
$ python manage.py runserver
```


### Start the client

The client will be available at http://localhost:8080

```sh
$ cd webtasks
$ cd client
$ http-server
```


## Testing

### Without coverage:

```sh
$ export APP_SETTINGS="project.config.TestingConfig"
$ python manage.py test
```

### With coverage:

```sh
$ export APP_SETTINGS="project.config.TestingConfig"
$ python manage.py cov
```
