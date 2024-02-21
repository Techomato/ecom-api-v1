
# AUTH
![](https://img.shields.io/badge/Python-3.11-green.svg)





An API layer to authenticate users, sellers and admins.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Installation

Clone the Git repository `auth`

`https://github.com/KoushikMallik-developer/auth-v2.git`

Create your virtual-environment for `auth` outside of the project root directory.

```bash
  python -m venv auth-env
  cd auth-env
  .\auth-env\Scripts\activate
```
Activate the environment.

```bash
  .\auth-env\Scripts\activate
```
Now install all the dependencies in auth-env.

```bash
  pip install -r .\dependencies\dev-requirements.txt
```
Go to project directory.
 
```bash
  cd auth
```

Rename the file `test.env` to `.env`

Run the below commands to make the migrations for database models.

```bash
  python .\manage.py makemigrations
  python .\manage.py migrate
```
Redis-Windows download:
```https://github.com/tporadowski/redis/releases/download/v5.0.14.1/Redis-x64-5.0.14.1.msi```

Install Redis using the installer downloaded.
Add redis in env var.

Run redis-cli in cmd
```bash
  redis-cli
  ping
```

Run the server.

```bash
  python .\manage.py runserver 8080
```

## 🔗 Links
[Staging](https://auth-stg.onrender.com/)\
[Production](https://auth-shoppixa.onrender.com/)
