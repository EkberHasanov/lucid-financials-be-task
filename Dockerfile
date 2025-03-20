FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymysql

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/code"

CMD ["uvicorn", "code.main:app", "--host", "0.0.0.0", "--port", "8000"]