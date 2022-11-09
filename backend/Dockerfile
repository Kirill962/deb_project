FROM python:3.7-slim
WORKDIR /code
COPY requirements.txt .
RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip && pip install -r requirements.txt
COPY . ./
CMD ["python3", "manage.py", "runserver", "0:8000"]