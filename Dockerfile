FROM python:3.12-slim-bookworm as builder

WORKDIR /workspace

COPY requirements.lock requirements.lock

RUN sed '/^-e/d' requirements.lock > requirements.txt

RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./run.py ./run.py

EXPOSE 8501

ENTRYPOINT [ "./run.py" ]