# Your current Docker image 
FROM python:3.11


# Proceed as before
RUN pip install poetry

WORKDIR /code
COPY ./pyproject.toml ./poetry.lock*  /code/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["uvicorn", "src.server.index:app", "--host", "0.0.0.0", "--port", "8000"]
