FROM python:3.9-slim
WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install --upgrade -r requirements.txt

EXPOSE 8080

COPY /app /app

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]