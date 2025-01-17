# RITA: Automatic Framework for Designing of Resilient IoT Applications
This repository has the code and dataset used in the paper: RITA: Automatic Framework for Designing of Resilient IoT Applications.

> The paper can be downloaded [here](https://arxiv.org/abs/2411.18324)

# Authors
Luis Eduardo Pessoa, [Cristovao Iglesias](https://cristovaoiglesias.github.io/personalwebsite/), Claudio Miceli

# Abstract
Designing resilient Internet of Things (IoT) systems requires i) identification of IoT Critical Objects (ICOs) such as services, devices, and resources, ii) threat analysis, and iii) mitigation strategy selection. However, the traditional process for designing resilient IoT systems is still manual, leading to inefficiencies and increased risks. In addition, while tools such as ChatGPT could support this manual and highly error-prone process, their use raises concerns over data privacy, inconsistent outputs, and internet dependence. Therefore, we propose RITA, an automated, open-source framework that uses a fine-tuned
RoBERTa-based Named Entity Recognition (NER) model to iden- tify ICOs from IoT requirement documents, correlate threats, and recommend countermeasures. RITA operates entirely offline
and can be deployed on-site, safeguarding sensitive information and delivering consistent outputs that enhance standardization. In our empirical evaluation, RITA outperformed ChatGPT in four of seven ICO categories, particularly in actuator, sensor, network resource, and service identification, using both human-annotated and ChatGPT-generated test data. These findings indicate that RITA can improve resilient IoT design by effectively supporting key security operations, offering a practical solution for developing robust IoT architectures.

# Video on how to use the platform
A vídeo teaching how to use the platform can be found [here](https://youtu.be/A-FVh4axTW0).

# DEMO
A demo of the application can be found [here](https://z2tmmi7gluiwrwhi.anvil.app/UCOFWNH4K7EQ764VLMWPQ4QY).

# How to install locally
Execute the deploy scripts in order as follows:
1. Download the `target` folder from [here](https://drive.google.com/drive/folders/1YXzFSELHtAvrxN0QSF5c9BcdxdGw8MzN?usp=sharing) and place it inside the `ner_model` folder. The `target` folder contains the trained model and was not provided inside github due to it's size.
1. Execute database/deploy.sh
2. Execute client/deploy.sh
3. Execute backend/deploy.sh

# Empirical evaluation
The empirical evaluation was done using a dashboard, which can be found [here](https://docs.google.com/spreadsheets/d/1HwF4ugGoeMJudVAE3xCAkDk_m9fBt1qV1TElV7ACx1E/edit?usp=sharing).

# Model download
The trained model can be downloaded from [here](https://drive.google.com/drive/folders/1YXzFSELHtAvrxN0QSF5c9BcdxdGw8MzN?usp=sharing).

# Frontend Project Address
The address below enables any Anvil user to generate a copy of the frontend project:  

[CLONE RITA CLIENT](https://anvil.works/build#clone:Z2TMMI7GLUIWRWHI=7YPEZXURUBM5M4OE3Q5CJU6V)
