FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "streamlit run --server.port $PORT /usr/src/app/app.py"]