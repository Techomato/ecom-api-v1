
# ECOM-API
![](https://img.shields.io/badge/Python-3.11-green.svg)





ECOMAPI functions as the intermediary layer, facilitating communication between the UI and various microservices. It receives requests from the UI and orchestrates calls to the corresponding microservices. Upon receiving responses, ECOMAPI relays them back to the UI. This architecture centralizes API management, streamlining communication and enhancing scalability and maintainability.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Installation

Clone the Git repository `ecom-api-v1`

`https://github.com/KoushikMallik-developer/ecom-api-v1.git`

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

Run the server.

```bash
  python .\manage.py runserver 8080
```