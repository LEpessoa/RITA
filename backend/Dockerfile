FROM python:3.8.10

ADD backend/requirements.txt .
ADD ner_model ./ner_model

RUN pip install spacy-transformers
RUN pip install spacy==3.5.0
RUN pip install -r requirements.txt

ADD backend/src/anvil_server.py .

CMD ["python3","anvil_server.py"]
# CMD ["tail","-f","/dev/null"]
