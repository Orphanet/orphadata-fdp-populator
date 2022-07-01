FROM python:3.6.8

WORKDIR /usr/src/app

COPY ./ /usr/src/app

RUN pip install -r  /usr/src/app/requirements.txt

CMD ["python", "/usr/src/app/mainFAIRdata.py"]
