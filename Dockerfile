FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt && gunicorn --version

COPY . .

ENV PYTHONUNBUFFERED=1 

ENV PYTHONPATH=/app:/app/ecom

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecom.wsgi:application"]