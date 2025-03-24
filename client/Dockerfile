FROM python:3.9-slim

RUN pip install flask requests

COPY app.py /app/
WORKDIR /app

CMD ["python", "app.py"]