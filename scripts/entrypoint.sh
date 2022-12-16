#!/bin/sh
echo "starting entrypoint.sh"

if [ "$DATABASE_RDBMS" = "postgresql" ]
then
    echo "waiting for PostgreSQL..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi

mkdir -p ~/.aws

echo """[$AWS_PROFILE]
aws_access_key_id = $AWS_ACCESS_KEY_ID
aws_secret_access_key = $AWS_SECRET_ACCESS_KEY
""" > ~/.aws/credentials

echo """[$AWS_PROFILE]
region = $AWS_REGION
output = json
""" > ~/.aws/config

poetry run python /app/scripts/create_database.py

#poetry run python manage.py flush --no-input
poetry run python manage.py makemigrations
poetry run python manage.py migrate
#poetry run python manage.py collectstatic --no-input
poetry run python manage.py test -p "test_*.py" --verbosity 2
poetry run python manage.py check --deploy

exec "$@"
