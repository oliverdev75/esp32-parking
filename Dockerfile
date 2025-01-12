FROM python

WORKDIR /app

ADD . /app

RUN apt update && apt install python3-brlapi -y
RUN pip install Pillow
RUN pip install PyYAML
RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]