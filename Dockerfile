FROM python:3.13.5

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV BOT_TOKEN=8568851271:AAFL5qwFQ3LyA3BfvOt0RW_SqrvXUT66UfA
ENV PROVIDER_TOKEN=1744374395:TEST:3c16a8525286640bcd1f
ENV DB_URL=postgresql+asyncpg://dmitriymacbookairm4:8091@localhost:5432/CryptoTrifecta
ENV CURRENCY=RUB

CMD ["python", "app.py"]