Postgres is a Relational database

## Docker Postgres Setup

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


## DATA TYPES
- Boolean
- Character - CHAR(n), VARCHAR(N), TEXT
- Numeric - Integer, Floating-Point
  - Integer - SMALLINT, INTEGER, BIGINT, SERIAL
  - FLoating-point - float(n), real, float8, numeric(p,s) - p digits with s number after the decimal
- Temporal - DATE, TIME, timestamp, interval
  - DATE - dates
  - TIME - time of day
  - TIMESTAMP - both date and time
  - TIMESTAMPTZ - timezone-aware timestampp data type
  - INTERVAL - periods of times
- geometric data - box, line, point, lseg, polygon
  - box - rectangular box
  - line - set of points
  - lseg - line segment
  - polygon - closed geometric
- network address - inet, macaddr
  - inet - IP4 address
  - macaddr - MAC address
- UUID
  - contact_id  
    ```
    CREATE TABLE contacts (
      contact_id uuid DEFAULT uuid_generate_v4 (),
      first_name VARCHAR NOT NULL,
      last_name VARCHAR NOT NULL,
      email VARCHAR NOT NULL,
      phone VARCHAR,
      PRIMARY KEY (contact_id)
    );
    ````
- Array
- JSON
- hstore - key value pair
