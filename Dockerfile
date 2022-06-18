FROM python:3.8

WORKDIR /project

COPY settings.local.json settings.local.json
COPY src /project

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

CMD ["uvicorn", "secret_sharing_api.main:app", "--host", "0.0.0.0", "--port", "8000"]