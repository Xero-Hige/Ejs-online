apt update
apt install docker docker-ce docker-ce-cli
bash ./CleanContainers.sh
pip3 install -r requirements.txt
docker build . -t run-container
