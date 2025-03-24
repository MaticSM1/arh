#slika
FROM python:3.9-slim 

# vse kniznice
RUN pip install flask opencv-python-headless

# kopja
COPY app.py /app/
WORKDIR /app

# run
CMD ["python", "app.py"]
