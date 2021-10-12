FROM ubuntu:20.04
FROM python:3.8
WORKDIR .
COPY . .
COPY ./run.sh /

RUN pip3 install -r requirements.txt
RUN chmod 755 /run.sh
ENTRYPOINT ["/run.sh"]