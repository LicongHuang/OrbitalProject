ROM alpine:latest
RUN apk add gnupg bash curl make build-base vim

ENV PYTHONUNBUFFERED=1
RUN apk add python3 python3-dev py3-pip py3-wheel py3-setuptools
RUN python3 -m ensurepip
RUN pip3 install --upgrade pip setuptools

WORKDIR /root

ENTRYPOINT ["/bin/bash"]

