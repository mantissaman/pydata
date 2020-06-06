#!/bin/sh

if [[ -z "$POSTGRES_USER" ]]; then
    export POSTGRES_USER=postgres
fi
if [[ -z "$POSTGRES_PASSWORD" ]]; then
    export POSTGRES_PASSWORD='pa55word'
fi
if [[ -z "$POSTGRES_DB" ]]; then
    export POSTGRES_DB=postgres
fi

export SOFTCHASSIS_USER=alchemyuser
export SOFTCHASSIS_DB='alchemy'
export SOFTCHASSIS_PASSWORD='pa55word'

echo "Rebuilding local DB started..."
base="$(date +%s)"

psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" << EOSQL
	UPDATE pg_database SET datallowconn = 'false' WHERE datname = '$SOFTCHASSIS_DB';
	SELECT pg_terminate_backend(pid)
	FROM pg_stat_activity
	WHERE datname = '$SOFTCHASSIS_DB';
	DROP DATABASE IF EXISTS $SOFTCHASSIS_DB;
	DROP USER IF EXISTS $SOFTCHASSIS_USER;
EOSQL

psql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" << EOSQL
	CREATE USER $SOFTCHASSIS_USER with password '$SOFTCHASSIS_PASSWORD';
    CREATE DATABASE $SOFTCHASSIS_DB;
    GRANT ALL PRIVILEGES ON DATABASE $SOFTCHASSIS_DB TO $SOFTCHASSIS_USER;
	ALTER USER $SOFTCHASSIS_USER WITH SUPERUSER;

EOSQL

after="$(date +%s)"
elasped_seconds="$(expr $after - $base)"
echo "Full Database build successfully completed in $elasped_seconds seconds."