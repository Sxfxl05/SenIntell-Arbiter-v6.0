FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir fastapi uvicorn httpx pydantic transformers torch sentencepiece
COPY arbiter_server.py .
EXPOSE 8000
CMD ["python", "arbiter_server.py"]