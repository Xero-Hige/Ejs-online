apt update && apt install docker
bash ./CleanContainers.sh
pip3 install -r requirements.txt
docker build . -t run-container
