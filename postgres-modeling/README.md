# Data Modeling with Postgres

## Setup instructions

Create a virtual environment (with Python 3.8)

```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

Upgrade pip and install requirements

```bash
(.venv) $ python -m pip install --upgrade pip
(.venv) $ python -m pip install -r requirements.txt
```

Setup the default role and db

```bash
make dbrole
make db
```

# Connect to a remote PostgreSQL DB

```bash
$ psql \
   --host=some-domain.us-east-1.rds.amazonaws.com \
   --port=5432 \
   --username=some_user \
   --password \
   --dbname=some_db

# List databases
$ some_db=> \list

# Switch to database
$ some_db=> \c some_other_db

# List tables
$ some_db=> \dt

# Create DB
$ createdb -p 5432 -h some-domain.us-east-1.rds.amazonaws.com -e some_db -U some_user
```
