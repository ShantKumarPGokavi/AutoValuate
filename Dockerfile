FROM python:3.10-slim

WORKDIR /app

# Copy all repository contents into the container
COPY . /app

# Install dependencies if requirements.txt exists, otherwise install core requirements directly
RUN if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    else \
        pip install --no-cache-dir flask scikit-learn numpy joblib pytest; \
    fi

EXPOSE 5000

CMD ["python", "app.py"]