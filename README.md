# Unlimited Parts API

## Project setup with development dependencies

### Create virtual env

```
python3 -m venv env
```

### Install dependencies

```
pip3 install -r requirements.txt
```

### Run migrations

```
python3 manage.py migrate
```

## Run API

```
python3 manage.py runserver
```

## Run tests

```
python3 manage.py test
```

## Explore browsable API

After starting the API, the [browsable API](http://localhost:8000/) provides endpoints for:

- [Parts CRUD](http://localhost:8000/parts/)
- [Top description words](http://localhost:8000/top_part_description_words/)
