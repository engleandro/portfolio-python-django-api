echo "Build..."

poetry install --no-root
poetry run pre-commit install

echo "Linting..."

poetry run black --check .
poetry run isort .
poetry run flake8 .
poetry run bandit .

echo "Unit Testing..."

poetry run pytest -vv

echo "Django check..."

poetry run python manage.py test -p 'test_*.py' --verbosity=2
poetry run python manage.py check --deploy

echo "Pre-commit analysis..."

poetry run pre-commit run --all-files
