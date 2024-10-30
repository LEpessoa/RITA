FROM python:3.8.10

ADD backend/requirements.txt .
ADD ner_model/target/model-best ./model-best
ADD backend/src/anvil_server.py .

RUN pip install spacy-transformers
RUN pip install -r requirements.txt
RUN pip install spacy==3.5.0

RUN ls .
CMD ["python3","anvil_server.py","&&","tail","-f","/dev/null"]
