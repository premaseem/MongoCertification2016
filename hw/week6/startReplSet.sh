mkdir -p /data/rs1 /data/rs2 /data/rs3
mongod --replSet m101 --logpath "1.log" --dbpath /data/db1 --port 27017 --oplogSize 64 --fork --smallfiles
mongod --replSet m101 --logpath "2.log" --dbpath /data/db2 --port 27018 --oplogSize 64 --smallfiles --fork
mongod --replSet m101 --logpath "3.log" --dbpath /data/db3 --port 27019 --oplogSize 64 --smallfiles --fork



mongod --replSet m101 --dbpath /data/db1 --port 27017 --oplogSize 64


mongod --port 27017 --dbpath /data/db1 --replSet m101 &
mongod --port 27018 --dbpath /data/db2 --replSet m101 &
mongod --port 27019 --dbpath /data/db3 --replSet m101 &