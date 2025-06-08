FROM python:3.10-slim

WORKDIR /app

# Install system dependencies including MySQL
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY src/ .

EXPOSE 5000

CMD ["python", "app.py"]