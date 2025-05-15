FROM python:3.9-slim
RUN pip install flwr tensorflow pyspark
COPY . /app
WORKDIR /app
CMD ["python", "fl_client.py"]