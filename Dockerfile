FROM ubuntu/python:latest
RUN  apt update && apt upgrade -y && apt install python3-django python3-djangorestframework
RUN  /app/rbr_srv/ && cd /app/rbr_srv/
WORKDIR /app/rbr_srv
COPY rbr_srv/* /app/rbr_srv/
CMD ["python", "rbr_srv/manager.py","runserver","8000"]
EXPOSE 8000
