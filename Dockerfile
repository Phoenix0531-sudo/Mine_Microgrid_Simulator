# Streamlit web dashboard for microgrid simulation
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# Smoke test: verify imports (web UI will not render in build)
CMD ["python", "scripts/docker_smoke_test.py"]
