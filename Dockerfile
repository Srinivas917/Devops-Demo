FROM python:latest 

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt 

EXPOSE 80

ENV NAME Srinivas

CMD ["python","app.py"]