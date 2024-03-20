FROM python:3.12-slim-bookworm as builder

RUN apt-get update && apt-get install -y curl && apt-get clean

RUN ls

# install rye
RUN curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash

ENV PATH="/root/.rye/shims:${PATH}"

WORKDIR /workspace

# copy the rye project
COPY README.md requirements.lock requirements-dev.lock pyproject.toml LICENSE ./

RUN rye sync

FROM python:3.12-slim-bookworm

WORKDIR /workspace

COPY --from=builder /workspace/.venv ./.venv
COPY --from=builder /root/.rye /root/.rye
COPY src ./src
COPY run.py ./

RUN mkdir -p /workspace/config/templates

EXPOSE 8501

ENTRYPOINT [ "./run.py" ]