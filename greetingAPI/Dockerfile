FROM tiangolo/uwsgi-nginx-flask:flask

MAINTAINER Puneeth Reddy "puneethreddy20@gmail.com"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "greetingAPI.py" ]
