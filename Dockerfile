FROM python:3.7-slim-buster

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ ./src
COPY features/ .

# command to run on container start
CMD [ "uvicorn", "src.main_api:app", "--host", "0.0.0.0"]