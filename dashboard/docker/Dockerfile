FROM python:3.9.12-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r docker/requirements.txt
RUN pip install -e .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 ctxdashboard.app:server