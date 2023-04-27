FROM python:3-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
