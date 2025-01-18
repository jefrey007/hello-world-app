FROM python:3.9-alpine

RUN apk update && apk add --no-cache postgresql-dev

RUN pip install flask-cors

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
