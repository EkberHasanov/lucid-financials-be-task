FROM python:3.11-slim

WORKDIR /src

RUN mkdir app

COPY requirements.txt app/
RUN pip install --no-cache-dir -r app/requirements.txt

COPY . app/

ENV PYTHONPATH="${PYTHONPATH}:/app"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]