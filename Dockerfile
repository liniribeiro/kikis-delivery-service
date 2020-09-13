FROM python:slim-stretch

WORKDIR /srv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    make \
    tzdata \
    gcc \
    g++ \
    ca-certificates \
    wget && \
    update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone && \
    pip install -U awscli

ADD Pipfile Pipfile.lock ./

RUN pip install --no-cache -U pip pipenv && pipenv install --system

RUN apt-get remove --purge -y \
    gcc \
    g++ \
    wget && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y

ADD . .

EXPOSE 80

ENTRYPOINT ["make", "run_all"]