FROM python:3.11-slim-bookworm

WORKDIR /usr/src/app

COPY requirements.txt .
COPY migrate.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./migrate.py"]
