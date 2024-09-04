FROM python:3.11.9-slim

WORKDIR /app

COPY fixtube fixtube
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "fixtube:create_app()"]
