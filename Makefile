setup: requirements.txt
	pip install -r requirements.txt

run:
	flask --app NodeService --debug run --port 3001

clean:
	rm -rf __pycache__
