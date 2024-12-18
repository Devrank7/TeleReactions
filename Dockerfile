FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"
CMD ["python", "main.py"]
