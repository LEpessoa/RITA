deploy_backend:
	docker build -f ./backend/Dockerfile \
		-t rita_backend --no-cache .
	docker rm -f rita_backend || echo "no container to remove"
	docker run -d --name rita_backend \
		--network resilient_net \
		rita_backend
evaluate_model:
	python3 -m spacy evaluate ./ner_model/target/model-best ./ner_model/DOC_BINS/test.spacy
train_model:
	time python3 -m spacy train ./ner_model/config.cfg --output ./ner_model/target
platform_evaluation:
	python3 ./dataset/src/platform_evaluation.py
install_project_dependencies:
	python3 -m venv env \
		&& pip install --upgrade pip \
		&& pip install numpy spacy==3.5.0 spacy-legacy==3.0.12 spacy-loggers==1.0.4 \
		&& python3 -m spacy download en_core_web_trf \
		&& pip install -r dataset/requirements.txt \
		&& pip install -r backend/requirements.txt \
		&& pip install pandas