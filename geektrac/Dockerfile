FROM alpine:latest

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt
RUN rm -f requirements.txt

CMD python3 -m flask --app geektrac.run run --debug --host 0.0.0.0