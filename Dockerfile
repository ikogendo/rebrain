FROM ubuntu:noble
RUN apt-get update && apt-get install -y  python3 python3-pip python3-django python3-djangorestframework && rm -rf /var/lib/apt/lists/*
RUN  /app/rbr_srv/ && cd /app/rbr_srv/
WORKDIR /app/rbr_srv
COPY rbr_srv/* /app/rbr_srv/
CMD ["python", "rbr_srv/manager.py","runserver","8000"]
EXPOSE 8000
