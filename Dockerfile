FROM python:3.11.15-alpine3.23
RUN mkdir /src
WORKDIR /src
ADD . /src

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
# expose port
EXPOSE 5000
