CREATE SCHEMA Users;

CREATE TABLE Users.user (
  user_id int,
  pw_hash varchar(255),
  email varchar(255),
  portfolio_id int,
  created_ts TIMESTAMP,
  modified_ts TIMESTAMP
);

CREATE TABLE Users.portfolio (
  portfolio_id int,
  user_id int,
  symbol varchar(5),
  quantity int,
  created_ts TIMESTAMP,
  modified_ts TIMESTAMP
);

CREATE SCHEMA Stocks;


CREATE TABLE Stocks.price (
  symbol varchar(5),
  price numeric,
  price_ts TIMESTAMP,
  is_market_open boolean,
  created_ts TIMESTAMP,
  modified_ts TIMESTAMP
);
