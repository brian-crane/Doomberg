CREATE SCHEMA Users;

CREATE TABLE Users.user (
  user_id int,
  pw_hash varchar(255),
  email varchar(255),
  portfolio_id int,
  created_ts TIMESTAMP,
  modified_ts TIMESTAMP
);

CREATE TABLE Users.net_worth (
  user_id int,
  net_worth int,
  net_worth_ts varchar(5),
  quantity int,
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
  after_hours boolean,
  source varchar(255),
  created_ts TIMESTAMP,
  modified_ts TIMESTAMP
);
