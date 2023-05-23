FROM debian:bookworm-slim

RUN apt-get update && apt upgrade -y
RUN apt-get install -y python3 python3-pip python3-full vim
RUN apt-get install -y sqlite3 libsqlite3-dev

COPY requirements.txt /home
#RUN pip3 install -r /home/requirements.txt
COPY . /home

WORKDIR /home


ENTRYPOINT ["/bin/bash"]

#CMD ["./startupscript.sh"]

