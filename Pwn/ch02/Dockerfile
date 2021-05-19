FROM ubuntu:latest

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /ctf

COPY srcs/chall_2.bin .
COPY flag.txt .
COPY ynetd /opt

RUN chown -R root:root /ctf

USER ctf
EXPOSE 6876
CMD /opt/ynetd -p 6876 ./chall_2.bin
