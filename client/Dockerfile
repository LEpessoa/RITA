FROM python:3.8.10

ADD backend/requirements.txt .
ADD backend/src/anvil_server.py .
ADD client/rita_client/ ./rita_client
RUN pip install anvil-app-server

RUN apt update && apt upgrade -y
RUN apt install openjdk-11-jre -y

ENTRYPOINT ["/bin/bash","-c"]
CMD ["anvil-app-server --app=rita_client --uplink-key=somerandomeuplinkkey"]
# CMD ["tail","-f","/dev/null"]
