FROM python:3.11-slim

# Set runtime engine attributes
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=UTC

# Leverage layer caching for dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Map structural source elements
COPY . .

# Execution entrypoint target
CMD ["python", "graph_engine.py"]