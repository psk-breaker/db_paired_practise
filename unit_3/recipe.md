## 1. Extract nouns from the user stories or specification

```
As a person who loves to travel,
So I can find a nice place to stay
I want to see a list of all available spaces.

As a person who loves to travel,
So I can plan my budget
I want to see price information for each space.

As a person who loves to travel,
So I can find the right space
I want to see what facilities each space has.

As a person who loves to travel,
So I can find the right space
I want to see the location of each space.

```

```
Nouns:
bnb_spaces:
            facilities, 
            location, 
            price
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| bnb_spaces           | location, facilities, price |

Name of the table (always plural): `bnb_spaces`

Column names: `location`, `facilities`, `price`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
location: text
facilities: text
price: money
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE bnb_spaces (
  id SERIAL PRIMARY KEY,
  location TEXT,
  facilities TEXT,
  price MONEY
);
```

## 5. Create the table

DROP TABLE IF EXISTS bnb_spaces

CREATE TABLE bnb_spaces (
  id SERIAL PRIMARY KEY,
  location TEXT,
  facilities TEXT,
  price MONEY
);


INSERT INTO bnb_spaces (location, facilities, price) VALUES ('London', 'Ensuite', 1000000)
INSERT INTO bnb_spaces (location, facilities, price) VALUES ('Manchest', 'shared toilets', 250000)
INSERT INTO bnb_spaces (location, facilities, price) VALUES ('Bristol', 'Balcony', 1000)

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```