FROM python:2.7-alpine
LABEL maintainer="shreyanshpandey08@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk add --no-cache bash
ENTRYPOINT ["/bin/bash"]