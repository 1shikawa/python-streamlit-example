FROM python:3.9-slim-buster
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade -r requirements.txt

COPY . .
EXPOSE 4000
CMD ["streamlit", "run", "/app/app.py", "--server.port", "4000"]
