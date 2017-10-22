# Mapified

Built on top of `aiohttp`, `aiomysql`, `aiomcache` and bunch of other `aio-*` libs.

## Build Setup
First of all back-end part consists of three modules:

1. **MySQL** backend

2. **Memcached** backend

3. **SMTP** backend

`Python` version required `>=3.5`. Before start, please install all
requirements with following command:

`pip install -r requirements.txt`

## MySQL backend

First of all you need to install MySQL on your OS. On **Windows** you can do this by
downloading appropriate version on [official site](https://dev.mysql.com/downloads/).

If you are on **Linux** you must download using following command:

```
sudo apt-get install mysql-server
sudo apt-get install mysql-client
```

Next you must create own schema and call it how you like. 
For example `myschema`.
Then create MySQL `user` and grant him all privileges to newly created
schema.

For example, `user` would be `user` with password of `testtest`.

Then create `.yaml` file in `/server/` directory. Structure should be same
as `config.example.yaml`.

Fill in all parameters in config's MySQL section. Config then should look like:

```
mysql:
  user: user
  password: testtest
  db: myschema
  host: localhost
  port: 3306
```

That's it. Now in order to create tables, you must run `deploy.py` script
located inside of `/server/` directory.

Run script like this (assuming you are already inside of `server` directory):

`python deploy.py --action=db_import`

If you would like to quickly drop all tables in schema you can run
same script with different `action` argument like this:

`python deploy.py --action=drop_tables`

This will create basic **DB** structure.

## Memcached backend

This backend is optional. Currently if you would like to mock all Cache
methods, simply provide `DEBUG` environment with value of `True`.
This will mock all Cache method to return `None` instead, and application
would use **DB** as much as possible.

In order to set up Memcached server, please download it from [this site](https://commaster.net/content/installing-memcached-windows):

And run it using following command (assuming you're on Windows):

`./memcached.exe`

If you're on Linux, you can use following command:

`apt-get install memcached`

That's it. This will install and start `Memcached` server on `11211` port (by default).

If you need to flush all keys in `Memcached`, simply do:

```bash
telnet 127.0.0.1:11211
flush_all
```

Then fill in `Memcached backend` parameters in appropriate section in
config like this:

```yaml
cache:
  host: 127.0.0.1
  port: 11211
```

## SMTP backend

This part is pretty trivial, since we use high-level API and 
Google's SMTP server for sending emails. Simply fill in fields in config
like this:

```yaml
email:
  user: username
  password: password
  host: smtp.gmail.com
  port: 587
``` 

Assuming you have registered an account in [gmail.com](gmail.com).
