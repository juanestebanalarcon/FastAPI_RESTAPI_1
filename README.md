# FastAPI - RESTApi project
- Small RESTful API with crud operations.

# Technologies:

* Python:
    * fastapi
    * uvicorn 
    * python-multipart

- Pipfile

```bash
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
fastapi = "*"
uvicorn = "*"
python-multipart = "*"
sqlalchemy = "*"
passlib = {extras = ["bcrypt"], version = "*"}
python-jose = {extras = ["cryptography"], version = "*"}
psycopg2-binary = "*"

[dev-packages]

[requires]
python_version = "3.10"


```
- Commands:

```bash
pipenv shell
pipenv install
uvicorn <filename>:app --reload
```