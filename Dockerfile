FROM ubuntu/python:3.12-24.04_stable
RUN  apt update && apt upgrade -y && apt install -y python3-django python3-djangorestframework
RUN  /app/rbr_srv/ && cd /app/rbr_srv/
WORKDIR /app/rbr_srv
COPY rbr_srv/* /app/rbr_srv/
CMD ["python", "rbr_srv/manager.py","runserver","8000"]
EXPOSE 8000
