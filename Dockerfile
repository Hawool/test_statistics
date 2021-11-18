FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app
WORKDIR /app/

COPY . /app/
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
