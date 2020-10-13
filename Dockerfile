FROM python:3
WORKDIR /root/

RUN pip install flask

COPY decoder.json /root/decoder.json
COPY encoded.txt /root/encoded.txt
COPY service.py /root/app.py

CMD ["python", "-u","/root/app.py"]