FROM python:3.6.5

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE=SlackNotifier.settings

COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python3 manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]