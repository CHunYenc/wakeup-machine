FROM python:3.8-alpine

LABEL author="op84a2546@gmail.com"

COPY . /app

WORKDIR /app

RUN apk add --no-cache make build-base

# Python
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "Your Website is $URL"

CMD [ "python", "app.py" ]