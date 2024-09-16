FROM python:3.12.6

# Create directory for the app user
RUN mkdir -p /app/infinitex

# Create the app user
RUN groupadd app && useradd -g app app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create the home directory
ENV APP_HOME=/app/infinitex
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# Install
COPY . $APP_HOME
RUN pip install --no-cache-dir --trusted-host pypi.org --upgrade pip
RUN pip install -r requirements.txt

RUN chown -R app:app $APP_HOME
#RUN python manage.py collectstatic --no-input --clear
USER app
