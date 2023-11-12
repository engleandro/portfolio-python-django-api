# CODE CHALLENGE: DJANGO-API

It is a result of a Code Challenge.

### API
- [x] POST endpoint that receives a JSON containing the lengths of the 3 sides of the triangle (/api/v1/triangles/)
- [x] Try it on POST /api/v1/triangles/ or /api/v1/doc/ after registering a user and login into the application.
- [x] API endpoint to get history from the database at GET /api/v1/triangles/ or by triangles app at /api/v1/doc/
- [ ] This solution is not on AWS API Gateway
- [x] Authentication is implemented. You should be authenticated to access the resources (/api/v1/registration/, /api/v1/login/ and /api/v1/token/).
- [x] Requests limitation / throttling mechanism is implemented at API- (admin.settings.py) or apiview level (apps.triangles.apiviews.py)

### CODE
- [x] It is implemented in Python. It has a little bash, SQL, YAML and Terraform syntaxes.
- [x] The input values are validated at model level by validators
- [x] The tests are implemented on Django tests: Unit Tests on /apps/triangles/tests/test_A....py
- [x] The tests are implemented on Django tests: Unit Tests on /apps/triangles/tests/test_B....py
- [ ] It was not based on BDD-style

### DATABASE
- [x] All the triangles are stored on the triangles table and you can get history from the database.
- [ ] It is not based on fully managed and cloud data solutions such as RDS or DynamoDB, but it can be easily transformed by creating a Posgres RDS and editing the .env file

### MONITORING
- [X] The application monitors the error logs
- [x] It is based on AWS CloudWatch
- [ ] The retention time is not configured on API level

## INFRASTRUCTURE
- [ ] The infrastructure as code with Terraform was incomplete and it was still in the configuration phase.

## DOCUMENTATION
- [x] You can easily run the application by reading this README file
- [x] You can easily run the test by reading this README file
- [x] The API documentation is available at /api/v1/doc/, /api/v1/redoc/ or /api/v1/apidoc/.

---

## SOURCES
* [AWS](https://aws.amazon.com/)
* [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [Install Docker and Docker-Compose](https://docs.docker.com/engine/install/ubuntu/)
* [Pyenv - Python Version Manager](https://github.com/pyenv/pyenv)
* [Poetry - Python Project and Package Manager](https://python-poetry.org/)
* [Pre-Commit - Python Linting](https://pre-commit.com/)
* [Django Framework](https://www.djangoproject.com/)
* [DJango Packages](https://djangopackages.org/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Django DRF YASG Documentation](https://drf-yasg.readthedocs.io/en/stable/)
* [Django Rest-Authorization](https://django-allauth.readthedocs.io/en/latest/installation.html)
* [Django Simple JSON Web Tokens](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* [Watchtower: Python CloudWatch Logging](https://kislyuk.github.io/watchtower/)
* [Postman - API platform for building and testing](https://www.postman.com/)

## GETTING STARTED

This project is an API platform based on Django-Python to provide restful back-end services on triangle analysis.

It provides a triangle classification based on the lengths of its three sides and gets a list of the last created triangles.

After running the application locally, use it by following:
* At web browser, find out more about this API at /api/v1/doc/ or /api/v1/redoc/
* At web browser, register a user at /api/v1/registration/
* At the web browser, log in with the user at /api/v1/login/. You need to be authenticated to use this API
* At the web browser, get the JWT token at /api/v1/token/ for Postman tests
* Or you can try out the resources related to the triangles app at /api/v1/triangles/
* Create a new triangle by sending a POST request to /api/v1/triangles/ with body={"edge1": 1, "edge2": 1.0, "edge3": 1.0,} and add to headers Authorization="Bearer generated-jwt-token"
* Get the last created triangles by sending a GET request to /api/v1/triangles/ and add to headers Authorization="Bearer generated-jwt-token"

Please, create a user and log in at the resources respectively:
* api/v1/registration/
* api/v1/login/

After that, look at the details of this API and its resources on EPs:
* /api/v1/doc/
* /api/v1/redoc/
* /api/v1/apidoc/

or you can try out the triangles app resources at:
* /api/v1/triangles/
* /api/v1/doc/

You can consume the API by generating a JWT token and testing it with [Postman](https://www.postman.com/):
* api/v1/token/

## INSTALL & CONFIGURE

Prerequisites:
* [docker and docker-compose](https://docs.docker.com/engine/install/ubuntu/)
* Create an AWS account, create an IAM User with CloudWatchLogsFullAccess, and configure a default profile for AWS CLI
* Edit the .env[model] to .env with the your information

Run Dockery:

```shell
docker compose down && docker compose up -d
```

## DEVELOPER'S GUIDE

The original idea about this solution was:
* A cloud-based API (API Gateway, ECS, EKS, ALB, AutoScaling) based on Django-Python with Pyenv, Poetry, Pytest, Black, Flake8, Isort, Bandit, Pre-commit and so on.
* A relational database on Postgres (Amazon RDS) and a non-relational database for cache with Redis (Amazon ElastiCache).
* All the DevOps/DevSecOps on GitLAB with Gitlab CI/CDs and environments based on docker/kubernetes cluster.
* Cloud infrastructure managed by Terraform on Amazon Web Services (AWS).

The provided solution here is:
* A local-based API based on Django-Python with Pyenv, Poetry, Pytest, Black, Flake8, Isort, Bandit, Pre-commit, and so on.
* The local data solution is the same but based on Postgres and Redis containers
* The GitLab CI/CD pipeline is incomplete.
* The cloud infrastructure managed by Terraform is in the configuration phase and is incomplete.

The stacks on this project:
* Python (3.11), Pyenv, Poetry
* Python Libraries: Django, Django Rest Framework, drf-Yasg, many Django packages, redis, psycopg, boto3, Watchtower, pytest.
* Documentation: Django DRF YASG documentation (Swagger and openapi)
* Servers: Django test server and gunicorn
* Linting tools: Black, Flake8, Isort, Bandit, Pre-commit
* Testing tools: Pytest, Django Testing
* DevOps tools: git, GitLab, docker, docker-compose, GitLab CI/CD
* Cloud tools: AWS and Terraform

After installing and configuring it, run the application:

```shell
docker compose down && docker compose up -d
```

All the resource details about the API are provided in the documentation:
* http://localhost:8000/api/v1/doc/
* http://localhost:8000/api/v1/redoc/
* http://localhost:8000/api/v1/apidoc/

To check on the triangle app on Django-based API:
* http://localhost:8000/api/v1/triangles/
* http://localhost:8000/api/v1/doc/

but you should register a user and log in to the application first.

All the errors on the application are sent to AWS CloudWatch by watchtower on .env[AWS_CLOUDWATCH_LOG_GROUP] log_group.

To build, lint, and test it locally:

```shell
cd "path/to/the/project"

echo "install pyenv"
pyenv install

echo "Build..."

poetry install --no-root
poetry run pre-commit install

echo "Linting..."

poetry run black --check .
poetry run isort .
poetry run flake8 .
poetry run bandit .

echo "Unit Testing with Pytest..."

poetry run pytest -vv

echo "Django check..."

poetry run python manage.py test -p 'test_*.py' --verbosity=2
poetry run python manage.py check --deploy

echo "Pre-commit analysis..."

poetry run pre-commit run --all-files
```

You can use [Postman](https://www.postman.com/) to test it in more detail.

Any doubt, please check on the documentation and/or contact me (alves.engleandro@gmail.com).

## QUALITY STANDARDS

Not available yet.
