# docker
docker-compose up -d
docker-compose down

# python venv
python3 -m venv venv
source venv/bin/activate

# hadoop
start-all.sh
stop-all.sh

# mysql
docker-compose -f docker-compose-mysql.yml up -d
   docker exec -it mysql-source mysql -u root -p
