# Question Corrector

## Instructions

### Backend

1. Create a virtual environment and activate it.
```bash
python -m venv venv
```
```bash
./venv/Scripts/activate
```

1. Install dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

1. make migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

1. Run the server.
```bash
python manage.py runserver
```

### Postgres

create a postgres server and database, change the settings in `settings.py` to match your database.
