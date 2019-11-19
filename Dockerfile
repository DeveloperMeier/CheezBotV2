FROM python:3.7

COPY . /home/app
WORKDIR /home/app

RUN pip install -r requirements.txt

CMD  python main.py
