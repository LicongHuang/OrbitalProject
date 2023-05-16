FROM debian:bookworm-slim

RUN apt-get update && apt upgrade -y
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y sqlite3 libsqlite3-dev

WORKDIR /root

ENTRYPOINT ["/bin/bash"]

