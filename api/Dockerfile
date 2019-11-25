FROM python:3.6

WORKDIR /app/api

COPY . /app/api

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:$PORT
