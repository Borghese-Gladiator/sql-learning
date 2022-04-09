# SQL Learning
Learn SQL using local Docker Setup and free online courses (W3Schools)

## Docker Setup

### Docker Compose Setup
https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5
- docker compose up
- open http://localhost:5050/ and login (admin@admin.com / root)
- Add New Server
  - Name - my_db
  - Host name/address - pg_container
  - Username - root
  - Password - root

### Docker Commands Setup
https://towardsdatascience.com/local-development-set-up-of-postgresql-with-docker-c022632f13ea

#### Postgres Steps
- mkdir ${HOME}/postgres-data/
- docker pull postgres
- run container
	- WINDOWS - docker run -d --name dev-postgres -e POSTGRES_PASSWORD=Pass2020! -v C:/Users/Timot/Downloads/postgres-data/:/var/lib/postgresql/data -p 5432:5432 postgres
	- LINUX - docker run -d \
		--name dev-postgres \
		-e POSTGRES_PASSWORD=Pass2020! \
		-v ${HOME}/postgres-data/:/var/lib/postgresql/data \
			-p 5432:5432
			postgres
- docker ps
- docker exec -it dev-postgres bash
- psql -h localhost -U postgres
- \l

#### pgAdmin steps
- docker pull dpage/pgadmin4
- run container
	- WINDOWS - docker run -p 80:80 -e PGADMIN_DEFAULT_EMAIL=user@domain.local -e PGADMIN_DEFAULT_PASSWORD=SuperSecret --name dev-pgadmin -d dpage/pgadmin4
	- LINUX - docker run \ 
		-p 80:80 \
		-e 'PGADMIN_DEFAULT_EMAIL=user@domain.local' \
		-e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
		--name dev-pgadmin \ 
		-d dpage/pgadmin4

#### View Postgres DB in pgAdmin
- Get IP Address of Postgres - docker inspect dev-postgres -f "{{json .NetworkSettings.Networks }}"
- Enter email - user@domain.local
- Enter password - SuperSecret
- Add New Server
	- Name - First Postgres Server
	- Connection - <IP Address>
	- Username - postgres
	- Password - Pass2020!
