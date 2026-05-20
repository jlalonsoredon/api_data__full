FROM python:3.11-slim
RUN mkdir /src
WORKDIR /src
ADD . /src

RUN pip install -r requirements.txt

# expose port
EXPOSE 5001

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
