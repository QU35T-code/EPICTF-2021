FROM python:3.9
WORKDIR /pokemon
COPY . /pokemon
RUN pip3 install Flask
RUN pip3 install requests
RUN pip3 install flask-mysqldb
EXPOSE 9327
CMD python3 main.py
