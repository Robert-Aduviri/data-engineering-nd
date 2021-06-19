# Data Modeling with Postgres

This project involves defining fact and dimension tables following a star schema
for a particular analytic focus, and writing an ETL pipeline that transfers data
from files in two local directories into these tables in Postgres using Python and SQL.

More details about the project scenario and context can be found in
the project [context](Project_context.md) file

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

## Usage instructions

Once the setup is finished, you can create the tables using the following
[Makefile](Makefile) target:

```bash
make tables
```

After this, you can load data from the user event logs (`data/log_data`) and the
Million Song Dataset subset (`data/song_data`) using the following
[Makefile](Makefile) target:

```bash
make data
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
