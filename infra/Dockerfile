FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY ["canary_analyzer.py", "canary_analyzer.py"]
COPY ["sample_canaries.csv", "sample_canaries.csv"]
USER 10001:10001
CMD ["python", "canary_analyzer.py", "sample_canaries.csv", "--json"]
