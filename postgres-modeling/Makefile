.PHONY: tables data start-pg stop-pg dbrole db

tables:
	python create_tables.py

data:
	python etl.py

# https://stackoverflow.com/questions/7975556/how-can-i-start-postgresql-server-on-mac-os-x

start-pg:
	pg_ctl -D /usr/local/var/postgres start

stop-pg:
	pg_ctl -D /usr/local/var/postgres stop

# https://stackoverflow.com/questions/11919391/postgresql-error-fatal-role-username-does-not-exist

dbrole:
	sudo -u robert createuser -s student

db:
	createdb -e studentdb -U student
