echo "Build..."

poetry install --only dev --no-root

echo "Linting..."

poetry run black --check main/
poetry run black --check apps/
poetry run black --check tests/
poetry run isort main/
poetry run isort apps/
poetry run isort tests/
poetry run flake8

poetry run bandit -r main
poetry run bandit -r apps
poetry run bandit -r tests

echo "Django check..."

poetry run python manage.py test
poetry run python manage.py check --deploy

echo "Unit Testing..."

poetry run pytest -vv
