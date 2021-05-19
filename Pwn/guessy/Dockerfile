FROM ubuntu:latest

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /ctf

COPY srcs/guessy.bin .
COPY flag.txt .
COPY ynetd /opt

RUN chown -R root:root /ctf

USER ctf
EXPOSE 6885
CMD /opt/ynetd -p 6885 ./guessy.bin
