# mysql
docker-compose -f docker-compose-mysql.yml up -d
docker exec -it mysql-source mysql -u root -p

# docker
docker-compose up -d
docker-compose down

# python venv
python3.10 -m venv venv
source venv/bin/activate
source deactivate

# hadoop
start-all.sh
stop-all.sh

# hive
rm -rf /Users/phucnt/metastore_db
schematool -initSchema -dbType derby

hive --service metastore &
hive