FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir requests
COPY arbiter_simulator.py .
CMD ["python", "arbiter_simulator.py"]