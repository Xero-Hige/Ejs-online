bash ./CleanContainers.sh
pip3 install -r requirements.txt
docker build . -t run-container
export NOMBRE_VENV=VALOR
gunicorn --bind 0.0.0.0:8000 app:app
