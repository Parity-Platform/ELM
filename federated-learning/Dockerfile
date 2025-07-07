FROM icos/dp-exec:latest
RUN pip install flwr tensorflow pyspark
COPY . /app
WORKDIR /app
ENV APP_PATH="/app"
CMD ["python", "fl_client.py"]
