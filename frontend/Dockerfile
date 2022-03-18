FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --upgrade -r requirements.txt

COPY . ./app
EXPOSE 4000
CMD ["streamlit", "run", "app.py", "--server.port", "4000"]
