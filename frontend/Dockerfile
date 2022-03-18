FROM python:3.9-slim
RUN pip3 install --upgrade -r requirements.txt
WORKDIR /app
COPY . ./app
EXPOSE 4000
CMD ["streamlit", "run", "app.py", "--server.port", "4000"]
