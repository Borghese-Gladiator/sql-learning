PgAdmin is a GUI tool to view Relational databases

## pgAdmin steps
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
