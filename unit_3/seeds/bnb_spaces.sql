
DROP TABLE IF EXISTS bnb_spaces;

CREATE TABLE bnb_spaces (
  id SERIAL PRIMARY KEY,
  location TEXT,
  facilities TEXT,
  price MONEY
);

INSERT INTO bnb_spaces (location, facilities, price) VALUES ('London', 'Ensuite', 1000000);
INSERT INTO bnb_spaces (location, facilities, price) VALUES ('Manchest', 'shared toilets', 250000);
INSERT INTO bnb_spaces (location, facilities, price) VALUES ('Bristol', 'Balcony', 1000);
