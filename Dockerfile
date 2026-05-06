FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT