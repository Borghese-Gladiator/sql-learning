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
