FROM ubuntu:focal

RUN apt-get update && apt upgrade -y
RUN apt-get install -y python3 python3-pip vim
RUN apt-get install -y sqlite3 libsqlite3-dev python3-pytest
RUN apt-get install -y usbutils udev

COPY . /home

WORKDIR /home

RUN pip3 install -r /home/requirements.txt


ENTRYPOINT ["/bin/bash"]

#CMD ["./startupscript.sh"]

