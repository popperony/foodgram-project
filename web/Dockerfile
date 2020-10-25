FROM python:3.8.5

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

COPY . /code

RUN python ./foodgram/manage.py collectstatic --noinput
